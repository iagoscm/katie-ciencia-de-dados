def aluguel_carro(km, dias):
    dias *= 60.0
    if (dias == 0):
        dias = 60.0
    km *= 0.15
    valor = km+dias
    print("O valor a ser pago sera de",valor, "reais")

dias = int(input("Digite a quantidade de dias de aluguel: "))
km = float(input("Digite a kilometragem percorrida: "))
aluguel_carro(km, dias)
