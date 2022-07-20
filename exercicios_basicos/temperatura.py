def conversor_ctof(c):
    f = 9*c
    f /= 5
    f += 32
    print("A temperatura de %.1f ºC eh equivalente a" % c,f, "ºF")

c = float(input("Digite a temperatura em celsius: "))
conversor_ctof(c)
