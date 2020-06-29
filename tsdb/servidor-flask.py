# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

from flask import Flask, request
app = Flask(__name__)


@app.route("/gravar", methods=["POST"])
def gravar():
    # Endpoint de gravação de dados no InfluxDB.
    # Ao receber a requisição, são verificados os campos JSON
    # para validação antes de escrever propriamente no banco.

    # Verificar se o tipo de conteúdo (payload) é JSON.
    # No caso, o cabeçalho HTTP 'Content-Type: application/json'.
    if request.is_json:
        # Testar (try) a leitura do JSON. Pode dar errado, logo é
        # necessário um bloco com tratamento de falha.
        try:
            # Se o cabeçalho for válido, prosseguir lendo os dados.
            req = request.get_json()
        except:
            # Em caso contrário, retornar 400.
            resposta = {"Erro": "JSON inválido"}
            return resposta, 400

        # Verificar se a chave 'medida' consta no JSON.
        if "medida" not in req:
            # Em caso contrário, retornar 400.
            resposta = {"Erro": "Campo 'medida' inexistente."}
            return resposta, 400
        else:
            # 'medida' existe, agora é preciso verificar se é string.
            if type(req["medida"]) is not str:
                # Em caso contrário, retornar 400.
                resposta = {"Erro": "Campo 'medida' deve ser string."}
                return resposta, 400

        # Verificar se a chave 'valores' consta no JSON.
        if "valores" not in req:
            # Em caso contrário, retornar 400.
            resposta = {"Erro": "Campo 'valores' inexistente."}
            return resposta, 400
        else:
            # 'valores' existe, agora é preciso verificar se existe pelo menos
            # 1 par chave-valor.
            if type(req["valores"]) is not list or len(req["valores"]) < 1:
                # Em caso contrário, retornar 400.
                resposta = {
                    "Erro": "Campo 'valores' deve ser uma lista não vazia."}
                return resposta, 400

        # Se todas as verificações foram feitas, retornar 200.
        resposta = {"Sucesso": "JSON válido."}
        return resposta, 200
    else:
        # Em caso contrário, retornar 400.
        resposta = {
            "Erro": "Tipo de conteúdo não definido como JSON."}
        return resposta, 400
