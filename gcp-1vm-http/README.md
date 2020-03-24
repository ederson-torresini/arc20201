# gcp-1m-http

Este modelo define uma máquina virtual no Google Cloud com acesso a HTTP/HTTPS e IPv4 fixo.

Para usar, é preciso criar o arquivo de variáveis do Terraform, no seguinte formato:

```
gcp_sakey = "***"
gce_project = "***"
gce_region = "***"
gce_zone = "***"
gce_ssh_user = "***"
gce_ssh_pub_key = "***"
```

onde:
- `gcp_sakey`: é a [chave de conta de serviço criada na GCP](https://console.cloud.google.com/apis/credentials/serviceaccountkey), em formato JSON.
- `gce_project`: nome do projeto.
- `gce_region`: região onde rodará a máquina virtual.
- `gce_zone`: dependente de `gce_region`, é a zona específica na região.
- `gce_ssh_user`: nome do usuário a ser criado dentro da máquina virtual.
- `gce_ssh_pub_key`: conteúdo do arquivo da chave pública SSH (não o nome do arquivo).

Exemplo de cenário a rodar na zona A de São Paulo:

```
gcp_sakey = "gcp.json"
gce_project = "teste-123456"
gce_region = "southamerica-east1"
gce_zone = "southamerica-east1-a"
gce_ssh_user = "boidacarapreta"
gce_ssh_pub_key_file = "ssh-rsa AAA...xWQ== ederson@boidacarapreta.cc"
```

## Como usar

Para facilitar o dia a dia, há o arquivo `Makefile`, que pode criar todo o ambiente:

```
make create
```

ou destrui-lo:

```
make destroy
```

O retorno será o IPv4 para se conectar via SSH.

## Nota

A configuração do Terraform, `gcp.tf`, é compatível com [versão 0.12 ou superior](https://www.terraform.io/docs/configuration/).
