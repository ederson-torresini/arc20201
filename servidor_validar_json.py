def validar_json(dados):
    # Verificar se os campos obrigatórios do JSON constam e são válidos.

    # A princípio, assume-se que o JSON é válido,
    # o código HTTP de resposta é 204 (No Context)
    # , uma vez que e a URL é desconhecida (None)
    resposta = {"Sucesso": "JSON válido."}
    http_status = 204
    codinome = None
    url = None

    # Verificar se a chave 'medida' consta no JSON.
    if "medida" not in dados:
        # Em caso contrário, retornar 400.
        resposta = {"Erro": "Campo 'medida' inexistente."}
        http_status = 400
    else:
        # 'medida' existe, agora é preciso verificar se é string.
        if type(dados["medida"]) != str:
            # Em caso contrário, retornar 400.
            resposta = {"Erro": "Campo 'medida' deve ser string."}
            http_status = 400
        else:
            # Verificar se a chave 'marcadores' consta no JSON.
            if "marcadores" in dados:
                # Primeiro, processar "marcadores" como uma lista de elementos.
                # No caso, item a item.
                for item in dados["marcadores"]:
                    # Segundo, processador cada item como um dicionário.
                    # No caso, um dicionário, sabidamente, de apenas um par chave-valor.
                    # Mas, de qualque forma, o código se aplica a um ou mais pares.
                    # Há formas ainda mais sintéticas e elegantes, como em:
                    # https://www.geeksforgeeks.org/python-convert-dictionary-to-concatenated-string
                    # Porém, manteremos o formato mais linear por questões didáticas.
                    for chave, valor in item.items():
                        # Adicionar, ao final da string, o formato: "," + chave + "=" + valor.
                        if chave.lower() == "codinome":
                            codinome = valor
                        if chave.lower() == "url":
                            url = valor
                if codinome and url:
                    http_status = 201
            # Verificar se a chave 'valores' consta no JSON.
            if "valores" not in dados:
                # Em caso contrário, retornar 400.
                resposta = {"Erro": "Campo 'valores' inexistente."}
                http_status = 400
            else:
                # 'valores' existe, agora é preciso verificar se existe pelo menos
                # 1 par chave-valor.
                if type(dados["valores"]) != list or len(dados["valores"]) < 1:
                    # Em caso contrário, retornar 400.
                    resposta = {
                        "Erro": "Campo 'valores' deve ser uma lista não vazia."}
                    http_status = 400

    # Se todas as verificações foram feitas, retornar sucesso (201 ou 204)
    return resposta, http_status, codinome, url
