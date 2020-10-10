# ARC 2020.1

Este ramo (*branch*) tem o código da API em produção do livro/jogo/apostila: [https://arc20201.boidacarapreta.cc](https://arc20201.boidacarapreta.cc).

## Passo zero: criar uma base de jogadores

Como formato básico do arquivo `jogadores.json`, cada jogador tem o nome, primeira e segunda chaves:

```json
{
  "jogadores": [
    {
      "nome": "augusto.oliveira",
      "chave1": "e***n",
      "chave2": "l****A"
    },
    {
      "nome": "brenda.soares",
      "chave1": "m***l",
      "chave2": "0****E"
    },
    {
      "nome": "bruna.teles",
      "chave1": "F***l",
      "chave2": "B****U"
    },
    {
      "nome": "bruno.maciel",
      "chave1": "S***P",
      "chave2": "A****Q"
    },
    {
      "nome": "enzo.schier",
      "chave1": "g***o",
      "chave2": "3****M"
    },
    {
      "nome": "fernanda.verdi",
      "chave1": "8***v",
      "chave2": "l****0"
    },
    {
      "nome": "guilherme.leal",
      "chave1": "X***Y",
      "chave2": "5****c"
    },
    {
      "nome": "isabella.possebon",
      "chave1": "W***7",
      "chave2": "W****E"
    },
    {
      "nome": "jennifer.alexandre",
      "chave1": "e***M",
      "chave2": "G****8"
    },
    {
      "nome": "joao.lange",
      "chave1": "K***i",
      "chave2": "C****o"
    },
    {
      "nome": "lilia.silva",
      "chave1": "p***9",
      "chave2": "G****Q"
    },
    {
      "nome": "lucas.bernardo",
      "chave1": "B***E",
      "chave2": "e****s"
    },
    {
      "nome": "lucas.fontes",
      "chave1": "I***V",
      "chave2": "E****g"
    },
    {
      "nome": "manuella.silva",
      "chave1": "l***3",
      "chave2": "D****M"
    },
    {
      "nome": "mateus.seemann",
      "chave1": "u***s",
      "chave2": "o****E"
    },
    {
      "nome": "matheus.santana",
      "chave1": "k***_",
      "chave2": "B****g"
    },
    {
      "nome": "nathally.nascimento",
      "chave1": "a***y",
      "chave2": "n****o"
    },
    {
      "nome": "pedro.fagundes",
      "chave1": "B***n",
      "chave2": "b****U"
    },
    {
      "nome": "thiago.amorim",
      "chave1": "h***X",
      "chave2": "Y****E"
    },
    {
      "nome": "vinicius.fidelix",
      "chave1": "c***0",
      "chave2": "i****A"
    },
    {
      "nome": "wesley.pereira",
      "chave1": "y***T",
      "chave2": "N****U"
    },
    {
      "nome": "yasmim.silveira",
      "chave1": "3***7",
      "chave2": "1****A"
    },
    {
      "nome": "ederson.torresini",
      "chave1": "I***S",
      "chave2": "c****U"
    }
  ]
}
```

## Passo um: publicar o código

Este código foi pensado para rodar em PaaS. Atualmente, está em produção na [Google App Engine](https://cloud.google.com/appengine): [https://api.arc20201.boidacarapreta.cc](https://api.arc20201.boidacarapreta.cc).
