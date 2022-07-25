def tempodevida_fumante(cigdia, ciganos):
    cigdia *= 10
    if (ciganos == 0):
        ciganos = 365
    ciganos *= 365
    cigdia *= ciganos
    cigdia /= 60
    cigdia /= 24
    print ("Parabens! Voce tem menos %d dias de vida!" % cigdia)

cigdia = int(input("Quantos cigarros voce fuma por dia? "))
ciganos = int(input("Por quantos anos voce fuma? "))
tempodevida_fumante(cigdia, ciganos)
