from requests import post
from json import dumps


def escrever(baseurl, org, bucket, token, dados):
    # Formatar a consulta
    url = "{}/api/v2/write?org={}&bucket={}".format(baseurl, org, bucket)
    cabeçalhos = {"Authorization": "Token {}".format(token)}

    # Criar os objetos da consulta e realizar, de fato, a operação de escrita (write)
    # no banco de dados.
    req = post(url, headers=cabeçalhos, data=dados)

    # Retornar para a aplicação principal apenas o código HTTP de retorno
    return req.status_code


def notificar(webhook, msg):
    cabeçalhos = {"Content-Type": "application/json; charset=UTF-8"}
    data = {"text": msg}
    req = post(webhook, headers=cabeçalhos, data=dumps(data))
    return req.status_code
