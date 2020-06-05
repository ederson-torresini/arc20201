# Carregar módulos
from os import environ
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Criar variáveis do servidor InfluxDB
token = environ.get('INFLUXDB_TOKEN')
org = environ.get('INFLUXDB_ORG')
bucket = environ.get('INFLUXDB_BUCKET')

# Criar os objetos da consulta
client = InfluxDBClient(url=environ.get('INFLUXDB_BASEURL'), token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Construir os dados a serem escritos no banco
data = "ideia,local=quarto,personagem=Lola,acao=curiosa latitude=-27.6084177,longitude=-48.6354691,altitude=80"

# Realizar, de fato, a operação de escrita no banco de dados
write_api.write(bucket, org, data)
