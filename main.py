import random

def jogar_dado():

    return random.randint(1, 6)

nome = input("Digite seu nome: ")

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
        "Partida",
    "Rua Oscar Freire",
    "Sorte",
    "Avenida Paulista",
    "Prisão",
    "Copacabana",
    "Cofre",
    "Ipanema"
]

print("\nCasa atual:")
print(tabuleiro[posicao])

rodada = 1

while rodada <= 10:

    print(f"\n===== RODADA {rodada} =====")

    input("\nPrecione ENTER para jogar o dado")

    dado = jogar_dado()

    print(f"Voçê tirou {dado}")

    posicao = posicao + dado

    if posicao >=len(tabuleiro):

        posicao = posicao - len(tabuleiro)

        dinheiro = dinheiro + 200

        print("Você passou pela partida!")
        print("Você ganhou $200!")

    print(f"Nova posição: {posicao}")

    print(f"Voçê parou em: {tabuleiro[posicao]}")

    print(f"Dinheiro atual: ${dinheiro}")

    print("\n--- VEZ DO BOT A ---")

    dado_bot = jogar_dado()

    print(f"Bot A tirou {dado_bot}")

    posicao_bot_a += dado_bot

    if posicao_bot_a >= len(tabuleiro):

        posicao_bot_a -= len(tabuleiro)

    print(f"Bot A parou em: {tabuleiro[posicao_bot_a]}")

    rodada +=1

print(f"\nTotal de casas: {len(tabuleiro)}")