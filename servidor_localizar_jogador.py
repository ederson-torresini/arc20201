import json


def localizar_jogador(codinome):

    with open("jogadores.json") as f:
        base = json.load(f)

    return next((jogador for jogador in base["jogadores"] if jogador["nome"] == codinome), None)
