"""
Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia
for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso
contrário imprima na tela "Você precisa trabalhar!"

Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e
guarde os resultados em uma lista

Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto
temperatura for maior que 35, imprima as temperaturas na tela

Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que
100, imprima os valores na tela, mas quando for encontrado o valor 23, interrompa a
execução do programa

Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável
for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista

Exercício 8 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são
3 erros.

    temperatura = float(input('Qual a temperatura? '))
    if temperatura > 30
    print('Vista roupas leves.')
    else
        print('Busque seus casacos.')

Exercício 9 - Faça um programa que conte quantas vezes a letra "r" aparece na frase
abaixo.

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela
não é tão brilhante como os sonhos, tem pelo menos a vantagem de
existir."
"""

def diaDaSemana(dia):
    if dia.lower() == "domingo" or dia.lower() == "sabado" or dia.lower() == "sábado":
        print("Hoje é dia de descanso")
    else:
        print("Você precisa trabalhar!")


#Exercicio 1
print("Exercicio 1:")
diaDaSemana(input("Digite o dia da semana: "))

#Exercicio 2
print("\nExercicio 2")
lista = ['Morango', 'Kiwi', 'Manga', 'Maracujá', 'Tomate']
for fruta in lista:
    if fruta.lower() == 'morango':
        print("Morango faz parte da lista!")

#Exercicio 3
print("\nExercicio 3")
tupla = (3,5,7,11)
lista = []
for i in tupla:
    temp = i*2
    lista.append(temp)
print(lista)

#Exercicio 4
print("\nExercicio 4")
for i in range(100,151):
    if i%2 == 0:
        print(i)

#Exercicio 5
print("\nExercicio 5")
temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura -= 1

#Exercicio 6
print("\nExercicio 6")
contador = 0
while contador < 100:
    if contador == 23:
        break;
    print(contador)
    contador += 1

#Exercicio 7
print("\nExercicio 7")
lista = []
var = 4
while var <= 20:
    lista.append(var)
    var += 2
print(lista)

#Exercicio 8
print("\nExercicio 8")
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
print("\nOs erros eram: \n1. faltaram dois pontos depois do if e do else\n2. o primeiro print não estava identado corretamente")

#Exercício 9
print("\nExercicio 9")
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
contador = 0
for caracter in frase:
    if caracter == 'r':
        contador += 1
print("O caracter 'r' aparece %d vezes\n" % contador)
