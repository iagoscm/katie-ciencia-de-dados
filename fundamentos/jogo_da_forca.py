palavra = input("Digite a palavra a ser adivinhada: ").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    chute=""
    for letra in palavra:
        chute += letra if letra in acertos else "."
    print(chute)
    if chute == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já digitou essa letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
        print("===========\n    ")
        print("|  O  " if erros >= 1 else "X")
        linha2 = "|"
        if erros == 2:
            linha2 = "|  |  "
        elif erros == 3:
            linha2 = "| \|  "
        elif erros >= 4:
            linha2 = "| \|/ "
        print("%s" % linha2)
        linha3 = "|"
        if erros == 5:
            linha3 += " /   "
        elif erros >= 6:
            linha3 += " / \ "
        print("%s" % linha3)
        print("\n===========")
        if erros == 6:
            print("Enforcado!")
            break
