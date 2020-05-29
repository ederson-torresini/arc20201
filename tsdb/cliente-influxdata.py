# Módulos
import os
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Variáveis do servidor InfluxDB
token = os.environ.get('INFLUXDB_TOKEN')
org = os.environ.get('INFLUXDB_ORG')
bucket = os.environ.get('INFLUXDB_BUCKET')

# Testar se as variáveis de ambiente foram criadas
if token is None or org is None:
    raise Exception(
        'Por favor, crie as variáveis de ambiente em https://gitpod.io/settings/. Obrigado!')

# Criar os objetos da consulta
client = InfluxDBClient(
    url=os.environ.get('INFLUXDB_BASEURL'), token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Construir os dados a serem escritos no banco
data = "ideia,local=sonho,personagem=Lola,ação=voando latitude=-27.6084177,longitude=-48.6354691,altitude=80"

# Realizar, de fato, a operação de escrita no banco de dados
write_api.write(bucket, org, data)
