# ARC 2020.1

Este ramo (*branch*) tem o código da API em produção do livro/jogo/apostila: [https://arc20201.boidacarapreta.cc](https://arc20201.boidacarapreta.cc).

## Passo zero: criar uma base de jogadores

Como formato básico do arquivo `jogadores.json`, cada jogador tem o nome, primeira e segunda chaves:

```json
{
  "jogadores": [
    {
      "nome.sobrenome": "***",
      "chave1": "***",
      "chave2": "***"
    },
    {
      "nome.sobrenome": "***",
      "chave1": "***",
      "chave2": "***"
    }
  ]
}
```

## Passo um: publicar o código

Este código foi pensado para rodar em PaaS. Atualmente, está em produção na [Google App Engine](https://cloud.google.com/appengine): [https://api.arc20201.boidacarapreta.cc](https://api.arc20201.boidacarapreta.cc).
