# Sobre este projeto

Este projeto se refere a um servidor HTTP de conteúdo estático usando Python 3 e Flask. Significa, portanto, que se o cliente solicitar um recurso, o Python 3 + Flask irá procurar pelo arquivo com este endereço e o entregará com o conteúdo integral (e resposta HTTP `200 OK`). Caso o servidor não localize o arquivo, deverá informar que não foi localizado (resposta HTTP `404 Not Found`).

## Como usar o Flask

### Etapa 1: instalar os módulos

Como boa prática em Python, recomenda-se usar o arquivo `requirements.txt` para informar todos os módulos necessários para o projeto. Para o servidor HTTP, apenas o módulo `flask` é necessário, conforme o arquivo.

No Gitpod a instalação dos módulos é facilitada com o módulo `pip` (já instalado previamente no Gitpod):

```bash
python3 -m pip install -r requirements.txt
```

Pode-se confirmar que o módulo e suas dependências estão devidamente instaladas:

```bash
python3 -m pip list
```

### Etapa 2: executar o servidor HTTP

O segundo e último passo é executar o servidor HTTP. Para isso, deve-se informar o arquivo com o código em Python na variável `FLASK_APP`:

```bash
FLASK_APP=servidor.py flask run
```

Para validar, pode-se usar tanto um cliente HTTP externo (navegador) exportando a porta (5000) ou usar a previsualização interna do próprio Gitpod.