def converter_json_line_protocol(json):
    # Converter JSON em InfluxDB v2.0 line protocol

    # Começar a linha com a medida (measurement)
    line_protocol = json["medida"]

    # Na sequência, adicionar os marcadores (quando houver)
    if "marcadores" in json:
        # Primeiro, processar "marcadores" como uma lista de elementos.
        # No caso, item a item.
        for item in json["marcadores"]:
            # Segundo, processador cada item como um dicionário.
            # No caso, um dicionário, sabidamente, de apenas um par chave-valor.
            # Mas, de qualque forma, o código se aplica a um ou mais pares.
            # Há formas ainda mais sintéticas e elegantes, como em:
            # https://www.geeksforgeeks.org/python-convert-dictionary-to-concatenated-string
            # Porém, manteremos o formato mais linear por questões didáticas.
            for chave, valor in item.items():
                # Adicionar, ao final da string, o formato: "," + chave + "=" + valor.
                line_protocol += ",{}={}".format(chave, valor)

    # Por fim, adicionar os valores (obrigatório pelo menos um).
    # Antes de mais nada, separar os marcadores dos valores por um espaço (" ").
    # Por causa disto, apenas o primeiro item da lista será processado.
    # Lembrando que em Computação a contagem começa a partir do zero.
    for item in json["valores"][:1]:
        for chave, valor in item.items():
            line_protocol += " {}={}".format(chave, valor)

    # Para o segundo e demais elementos, é preciso adicionar vírgula (",") ao invés de espaço.
    # Logo, serão processados os itens 1 em diante.
    # A partir daqui a lógica é a mesma de marcadores, então os comentários duplicados
    # serão suprimidos.
    for item in json["valores"][1:]:
        for chave, valor in item.items():
            line_protocol += ",{}={}".format(chave, valor)

    # Retornar os dados formatados para InfluxDB 2.0 line protocol:
    # "measurement,tags values"
    # Como neste exemplo:
    # "measurement,tag0=abc,tag1=def,tag2=fgh value0=100,value1=200,value2=300"
    return line_protocol
