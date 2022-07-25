def milimetros(m):
    res = m/1000
    print("%.2f milimetro(s) eh igual a %.2f metro(s)" % (m, res))

m = float(input("Digite o valor que sera convertido de milimetros para metros: "))

milimetros(m)
