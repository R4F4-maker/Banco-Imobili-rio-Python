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

rodada = 1

while rodada <= 3:

    print(f"\n===== RODADA {rodada} =====")

    input("\nPrecione ENTER para jogar o dado")

    dado = random.randint(1, 6)

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

    rodada +=1

print(f"\nTotal de casas: {len(tabuleiro)}")

def mostrar_linha():

    print("--------------------")

mostrar_linha()
print("MONOPOLY")
mostrar_linha()

def mostrar_jogador(nome):

    print(f"Jogador: {nome}")

mostrar_jogador("Israel")
mostrar_jogador("Bot A")
mostrar_jogador("Bot B")

def somar(a, b):

    return a + b

resultado = somar(10, 5)

print(resultado)