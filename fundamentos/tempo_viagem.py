def tempo_viagem(dist, vm):
    tempo = dist/vm
    print("O tempo de viagem sera de", int(tempo), "horas")

vm = float(input("Digite a velocidade media em km/h: "))
dist = float(input("Digite a kilometragem a percorrer: "))

tempo_viagem(dist, vm)
