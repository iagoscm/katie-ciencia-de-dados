def segundos(dias,hrs,min,seg):
    dias *= 24
    dias *= 60
    dias *= 60
    hrs *= 60
    hrs *= 60
    min *= 60
    seg += dias+hrs+min
    print("O total de segundos eh %.2f" % seg)

dias = int(input("Digite a quantidade de dias: "))
hrs = float(input("Digite a quantidade de horas: "))
min = float(input("Digite a quantidade de minutos: "))
seg = float(input("Digite a quantidade de segundos: "))

segundos(dias, hrs, min, seg)
