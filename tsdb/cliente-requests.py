# https://requests.readthedocs.io/pt_BR/latest/

# Carregar módulos
from os import environ
from requests import post


def escrever(baseurl, org, bucket, token, dados):
    # Formatar a consulta
    url = "{}/api/v2/write?org={}&bucket={}".format(baseurl, org, bucket)
    cabeçalhos = {"Authorization": "Token {}".format(token)}

    # Criar os objetos da consulta e realizar, de fato, a operação de escrita (write) no banco de dados
    req = post(url, headers=cabeçalhos, data=dados)

    # Retornar para a aplicação principal apenas o código HTTP de retorno
    return req.status_code


def ler(baseurl, org, token, intervalo):
    # Formatar a consulta
    url = "{}/api/v2/query?org={}".format(baseurl, org)
    cabeçalhos = {
        "Authorization": "Token {}".format(token),
        "Accept": "application/csv",
        "Content-type": "application/vnd.flux"
    }
    dados = "from(bucket:\"{}\") |> range(start:-{})".format(bucket, intervalo)

    # Criar os objetos da consulta e realizar, de fato, a operação de leitura (query) no banco de dados
    req = post(url, headers=cabeçalhos, data=dados)

    # Retornar para a aplicação principal o código HTTP de retorno e o conteúdo
    return req.status_code, req.content


if __name__ == "__main__":
    # Criar variáveis do servidor InfluxDB
    baseurl = environ.get("INFLUXDB_BASEURL")
    org = environ.get("INFLUXDB_ORG")
    bucket = environ.get("INFLUXDB_BUCKET")
    token = environ.get("INFLUXDB_TOKEN")
    dados = "ideia,local=quarto,personagem=Lola,acao=curiosa latitude=-27.6084177,longitude=-48.6354691,altitude=80"
    intervalo = "1m"

    # Escrita no banco
    escrita_codigo = escrever(baseurl, org, bucket, token, dados)
    # O InfluxDB retorna 204 quando a solicitação de escrita é aceita
    if escrita_codigo == 204:
        print("Operação de escrita realizada com sucesso!")
    else:
        print("Problemas com a operação de escrita (código {}).".format(
            escrita_codigo))

    # Leitura do banco com determinado intervalo
    leitura_codigo, leitura_resposta = ler(baseurl, org, token, intervalo)
    # O InfluxDB retorna 200 quando a solicitação de leitura é aceita
    if leitura_codigo == 200:
        # As linhas do banco são convertidas (decodificadas) em UTF-8 para apresentar no terminal
        print("\nOperação de leitura realizada com sucesso:")
        print(leitura_resposta.decode("utf-8"))
    else:
        print("Problemas com a operação de leitura (código {}).".format(
            leitura_codigo))
