# Sobre o Bind9 no Gitpod

Rodar um servidor DNS no Gitpod requer algumas modificações do padrão esperado. Afinal, é um contêiner sem privilégios de administrador - seja via `su` ou `sudo`.

## Rodar o servidor DNS

Para rodar o servidor, o comando a ser executado é:
```bash
named -4 -c /workspace/gitpod-io/dns/named.conf -g
```
Ou para quem já está com o terminal dentro deste diretório (`dns`):
```bash
named -4 -c named.conf -g
```

Em relação ao Bind9 tradicional, foram feitas as seguintes alterações:
1. Porta do servidor: ao invés de [53/UDP](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt), será utilizada a porta `1053` (adicionado 1000 para passar do limiar 1023 de [portas privilegiadas](https://www.w3.org/Daemon/User/Installation/PrivilegedPorts.html)). Isso foi aplicado nas linhas `listen-on` e `query-source` da seção `options` do arquivo `named.conf`.

1. Porta do RNDC (_Remote Name Daemon Control_): ao invés de [953/TCP]((https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt)), será utilizada a porta `1953` (mesma lógica). Na seção `controls` do arquivo `named.conf` está indicada a porta para operar em _loopback_.
1. Não foi possível utilizar os servidores raiz (_root servers_) para consultas em geral. O arquivo [root.hints](https://www.internic.net/domain/named.root), original do Bind9, será ignorado e foram configurados dois servidores como "intermediários" (_forwarders_): `1.1.1.1` e `8.8.8.8` (veja seção `forwarders` no arquivo `named.conf`).
1. O servidor rodará associado ao terminal. Ou seja, não rodará ao fundo (_background_), podendo assim ser manipulado pelo terminal do Gitpod.

### Rodar o controlador do servidor DNS

O RNDC permite o controle do servidor DNS. Ao invés de parar todo o servidor, podem ser realizadas ações mais pontuais, como atualizar apenas uma zona.

Pode ser executado da seguinte forma:
```bash
rndc -c /workspace/gitpod-io/dns/rndc.conf <comando>
```
Ou, para quem já está com o terminal dentro deste diretório (`dns`):
```bash
rndc -c rndc.conf <comando>
```

Os comandos para os experimentos básicos mais indicados são:
- `flush`: limpar a cache do servidor;
- `reload`: recarregar configuração e zonas;
- `status`: apresentar o estado do servidor.
- `stop`: parar o servidor;
- `trace`: incrementar em 1 o nível de depuração do servidor - bom para observar no terminal do servidor as consultas DNS em ação.

Exemplo de uso do comando `status`: 
```bash
rndc -c /workspace/gitpod-io/dns/rndc.conf status
```
Ou, para quem já está com o terminal dentro deste diretório (`dns`):
```bash
rndc -c rndc.conf status
```

Nota explicativa: o `rndc` utiliza uma chave de segurança para enviar os comandos para o servidor. Esta chave foi gerada com o comando `rndc-confgen`. Não é preciso executar este comando (novamente): o arquivo `rndc.conf` e as seções `key` e `controls` do arquivo `named.conf` já estão prontos para uso.

## Rodar o cliente DNS

Assim como o servidor, o cliente precisa informar qual servidor e porta de destino a ser usado, conforme dito [anteriormente](#Rodar_o_servidor_DNS):
```bash
dig -p 1053 @127.0.0.1 <consulta>
```

Logo, para fazer a consulta do registro `SOA` do domínio `ifsc.edu.br`, a consulta ficará assim:
```bash
dig -p 1053 @127.0.0.1 SOA ifsc.edu.br
```

## `tl;dr`

1. Abra dois terminais no Gitpod.
2. No primeiro terminal digite:
```bash
named -4 -c /workspace/gitpod-io/dns/named.conf -g
```
3. Aparecerão duas mensagens no canto inferior direito do Gitpod. Feche as duas no "X".
4. No segundo terminal faça as consultas, como por exemplo o registro `SOA` do domínio `ifsc.edu.br`:
```bash
dig -p 1053 @127.0.0.1 SOA ifsc.edu.br
```
