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