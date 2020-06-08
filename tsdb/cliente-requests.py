# https://requests.readthedocs.io/pt_BR/latest/

# Carregar módulos
from os import environ
from requests import post

# Criar variáveis do servidor InfluxDB
baseurl = environ.get('INFLUXDB_BASEURL')
token = environ.get('INFLUXDB_TOKEN')
org = environ.get('INFLUXDB_ORG')
bucket = environ.get('INFLUXDB_BUCKET')

# Formatar a consulta
url = "{}/api/v2/write?org={}&bucket={}".format(baseurl, org, bucket)
cabeçalhos = {"Authorization": "Token {}".format(token)}
dados = "ideia,local=quarto,personagem=Lola,acao=curiosa latitude=-27.6084177,longitude=-48.6354691,altitude=80"

# Criar os objetos da consulta e realizar, de fato, a operação de escrita no banco de dados
req = post(url, headers=cabeçalhos, data=dados)
print(req.status_code)
