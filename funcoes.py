# funcoes.py

import random

def jogar_dado():
    return random.randint(1, 6)


def mostrar_placar(
    nome,
    dinheiro,
    bots,
    dinheiro_bots,
    propriedades
):
    print("\n===== PLACAR =====")

    print(f"{nome}: ${dinheiro}")

    falidos = []

    for j in range(len(bots)):

        if dinheiro_bots[j] <= 0:

            falidos.append(bots[j])

            for nome_prop in propriedades:

                if propriedades[nome_prop]["dono"] == bots[j]:
                    propriedades[nome_prop]["dono"] = None

            dinheiro_bots[j] = -999999

        else:

            print(
                f"{bots[j]}: "
                f"${dinheiro_bots[j]}"
            )

    for bot in falidos:
        print(f"{bot}: FALIU!")

    print("==================")