from dotenv import load_dotenv
from os import environ
from flask import Flask, request, abort
from requests import post
from servidor_validar_json import validar_json
from servidor_converter_json_line_protocol import converter_json_line_protocol
from servidor_escrever import escrever

app = Flask(__name__)

# Se houver um arquivo .env, que é comum em ambientes de desenvolvimento
# como IDEs locais (a exemplo de Visual Studio Code), carregar os valores
# e usá-los como variáveis de ambiente.
load_dotenv()

# Seja via arquivo .env convertido para variáveis de ambiente, ou mesmo
# variáveis de ambiente em outras IDEs, como Gitpod, o próximo passo
# é carregar variáveis do servidor InfluxDB para este programa.
baseurl = environ.get("INFLUXDB_BASEURL")
org = environ.get("INFLUXDB_ORG")
bucket = environ.get("INFLUXDB_BUCKET")
token = environ.get("INFLUXDB_TOKEN")


@app.route("/")
def index():
    abort(404)


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
        else:
            # Os dados estão em JSON válido.
            # Prosseguindo para validar os campos.
            resposta, codigo = validar_json(req)
            # Se algum campo tem problema, retornar 400
            # para o cliente HTTP deste servidor.
            if codigo == 400:
                return resposta, codigo
            else:
                # Os dados estão corretos.
                # Hora de enviar ao banco e retornar à primeira aplicação se a
                # operação deu certo ou não.
                line_protocol = converter_json_line_protocol(req)
                escrita_codigo = escrever(
                    baseurl, org, bucket, token, line_protocol)
                # O InfluxDB retorna 204 quando a operação é realizada com
                # sucesso, e retorna uma resposta vazia (No Content).
                if escrita_codigo == 204:
                    # Retornar 200 OK para o cliente.
                    return req, 201
                else:
                    # Ainda há algum problema?
                    # Retornar 500, quando o servidor não sabe o que fazer
                    # (na verdade, é algo que veremos nas próximas aulas :)
                    return req, 500
    else:
        # Em caso contrário, retornar 400.
        resposta = {
            "Erro": "Tipo de conteúdo não definido como JSON."}
        return resposta, 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
