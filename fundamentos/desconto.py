def desconto(valor, perc):
    perc = valor*(perc/100.0)
    valor -= perc
    print("O desconto foi de R$%.2f e o novo valor a ser pago eh de R$%.2f" % (perc, valor))

valor = float(input("Digite o valor da mercadoria: "))
perc = float(input("Digite o percentual do desconto: "))

desconto(valor, perc)
