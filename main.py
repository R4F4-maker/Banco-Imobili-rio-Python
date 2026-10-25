import random

nome = input("Digite seu nome: ")

dinheiro = 1500
posicao = 0

print(f"Jogador: {nome}")
print(f"Dinheiro: ${dinheiro}")
print(f"Posição: {posicao}")

bots = [
    "Bot A",
    "Bot B",
    "Bot C",
    "Bot D",
]

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

input("\nPrecione ENTER para jogar o dado")

dado = random.randint(1, 6)

print(f"Voçê tirou {dado}")

posicao = posicao + dado

print(f"Nova posição: {posicao}")

print(f"Voçê parou em: {tabuleiro[posicao]}")