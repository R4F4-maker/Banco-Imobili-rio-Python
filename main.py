import random

def jogar_dado():

    return random.randint(1, 6)

nome = input("Digite seu nome: ")

if nome == "":
    nome = "Jogador"

dinheiro = 1500

posicao = 0
posicao_bot_a = 0

print(f"Jogador: {nome}")
print(f"Dinheiro: ${dinheiro}")
print(f"Posição: {posicao}")

bots = [
    "Bot A",
    "Bot B",
    "Bot C",
    "Bot D",
]

posicoes_bots = [0, 0, 0, 0]

print("\nBots na partida:")

for bot in bots:
    print(bot)

tabuleiro = [
    "Partida",                    # 0
    "Avenida Mediterranea",       # 1
    "Cofre",                      # 2
    "Avenida Baltica",            # 3
    "Imposto de Renda",           # 4
    "Ferrovia Reading",           # 5
    "Avenida Oriental",           # 6
    "Sorte",                      # 7
    "Avenida Vermont",            # 8
    "Avenida Connecticut",        # 9
    "Prisao",                     # 10
    "Praca St. Charles",          # 11
    "Companhia Eletrica",         # 12
    "Avenida dos Estados",        # 13
    "Avenida Virginia",           # 14
    "Ferrovia Pennsylvania",      # 15
    "Praca St. James",            # 16
    "Cofre",                      # 17
    "Avenida Tennessee",          # 18
    "Avenida Nova York",          # 19
    "Estacionamento Livre",       # 20
    "Avenida Kentucky",           # 21
    "Sorte",                      # 22
    "Avenida Indiana",            # 23
    "Avenida Illinois",           # 24
    "Ferrovia B&O",              # 25
    "Avenida Atlantica",          # 26
    "Avenida Ventnor",            # 27
    "Companhia de Agua",          # 28
    "Jardins Marvin",             # 29
    "Vá para a Prisao",           # 30
    "Avenida Pacifica",           # 31
    "Avenida Carolina do Norte",  # 32
    "Cofre",                      # 33
    "Avenida Pennsylvania",       # 34
    "Ferrovia Short Line",        # 35
    "Sorte",                      # 36
    "Praca Park Place",           # 37
    "Taxa de Luxo",               # 38
    "Calcadao Boardwalk"          # 39
]

propriedades = {
    "Avenida Mediterranea": {
        "preco": 60,
        "aluguel": 10,
        "dono": None
    },

    "Avenida Baltica": {
        "preco": 60,
        "aluguel": 20,
        "dono": None
    },

    "Avenida Oriental": {
        "preco": 100,
        "aluguel": 30,
        "dono": None
    }
}

print(f"Você parou em: {tabuleiro[posicao]}")

print("\nCasa atual:")
print(tabuleiro[posicao])

rodada = 1

while rodada <= 60:

    print(f"\n===== RODADA {rodada} =====")

    input("\nPressione ENTER para jogar o dado")

    dado = jogar_dado()

    print(f"Você tirou {dado}")

    posicao += dado

    if posicao >= len(tabuleiro):

        posicao -= len(tabuleiro)

        dinheiro += 200

        print("Você passou pela partida!")
        print("Você ganhou $200!")

    print(f"Nova posição: {posicao}")

    print(f"Você parou em: {tabuleiro[posicao]}")

    casa = tabuleiro[posicao]

    if casa in propriedades:

        prop = propriedades[casa]

        if prop["dono"] is None:

            print("Esta propriedade pode ser comprada!")

            resposta = input(
                "Deseja comprar? (s/n): "
            )

            if resposta == "s":

                dinheiro -= prop["preco"]

                prop["dono"] = nome

                print("Propriedade comprada!")

        else:

            print(
                f"A propriedade pertence a "
                f"{prop['dono']}"
            )

            if prop["dono"] == "Bot A":

                aluguel = prop["aluguel"]

                dinheiro -= aluguel

                print(
                    f"Você pagou "
                    f"${aluguel} "
                    f"para o Bot A!"
                )

                print(
                    f"Seu saldo agora é "
                    f"${dinheiro}"
                )

    print(f"Dinheiro atual: ${dinheiro}")

    print("\n--- VEZ DO BOT A ---")

    dado_bot = jogar_dado()

    print(f"Bot A tirou {dado_bot}")

    posicao_bot_a += dado_bot

    if posicao_bot_a >= len(tabuleiro):

        posicao_bot_a -= len(tabuleiro)

    print(
        f"Bot A parou em: "
        f"{tabuleiro[posicao_bot_a]}"
    )

    casa_bot = tabuleiro[posicao_bot_a]

    if casa_bot in propriedades:

        prop = propriedades[casa_bot]

        if prop["dono"] is None:

            prop["dono"] = "Bot A"

            print(f"Bot A comprou {casa_bot}")

        elif prop["dono"] == nome:

            aluguel = prop["aluguel"]

            dinheiro += aluguel

            print(f"Bot A pagou ${aluguel} de aluguel!")
            print(f"Seu saldo agora é: ${dinheiro}")

    print(f"Fim da rodada {rodada}")

    rodada += 1

print(f"\nTotal de casas: {len(tabuleiro)}")