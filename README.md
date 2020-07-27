# ARC 2020.1

Ambiente de prototipação com [Gitpod](https://gitpod.io).

## Passo zero: antes de criar o Gitpod

Antes de criar o Gitpod, é preciso criar as seguintes [variáveis de ambiente no Gitpod](https://gitpod.io/settings/):

| Name               | Value             | Organization/Repository |
| ------------------ | ----------------- | ----------------------- |
| `INFLUXDB_BASEURL` | URL do servidor   | Nível de acesso         |
| `INFLUXDB_BUCKET`  | _Bucket_ criado   | Nível de acesso         |
| `INFLUXDB_ORG`     | Organização       | Nível de acesso         |
| `INFLUXDB_TOKEN`   | _Token_ de acesso | `*/*`                   |

Exemplo:

| Name               | Value                                             | Organization/Repository |
| ------------------ | ------------------------------------------------- | ----------------------- |
| `INFLUXDB_BASEURL` | `https://us-central1-1.gcp.cloud2.influxdata.com` | `*/*`                   |
| `INFLUXDB_BUCKET`  | `ideias`                                          | `*/*`                   |
| `INFLUXDB_ORG`     | `abc`                                             | `*/*`                   |
| `INFLUXDB_TOKEN`   | `codigosecreto`                                   | `*/*`                   |

Uma vez criadas as variáveis de ambiente, o Gitpod rodará o cliente em Python ou REST API com estes valores.

## Passo um: como rodar o Gitpod

Este repositório está preparado para rodar o código em modo depuração, com o objetivo de facilitar o desenvolvimento. Basta clicar em:

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/boidacarapreta/arc20201)
