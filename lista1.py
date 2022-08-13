""" 
Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

Exercício 2 - Crie uma lista de 5 objetos e imprima-os na tela.

Exercício 3 - Crie duas strings e concatene as duas em uma terceira string.

Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois
utilize a função count do objeto tupla para verificar quantas vezes o número 4 aparece na tupla.

Exercício 5 - Crie um dicionário vazio e imprima na tela.

Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela.

Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela.

Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma
lista de 2 elementos numéricos. Imprima o dicionário na tela.

Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, o
segundo uma tupla de 2 elementos, o terceiro um dicionário com 2 chaves e 2 valores e o
quarto elemento um valor do tipo float. Imprima a lista na tela.

Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI' """

def imprime1a10():

    lista = [1,2,3,4,5,6,7,8,9,10]

    for n in lista:
        print(n)

def lista5objetos():

    x = 1
    objetos = ['unicornio','jonas brothers','controle remoto','serginho groisman', 'prior do bbb']
    for n in objetos:
        print("Objeto %d: %s" % (x, n))
        x+=1

def concatenaString():
    
    frase1 = "eu amo"
    frase2 = "a Alexia"
    frase3 = frase1 + " " + frase2
    print("Frase 1: %s\nFrase 2: %s\nFrase concatenada: %s" % (frase1, frase2, frase3))

def contaTupla():

    tupla = (1, 2, 2, 3, 4, 4, 4, 5)
    print("Quantidade de 4's na tupla: %d" % tupla.count(4))

def dicionarioVazio():

    dicionario = {}
    print(dicionario)

def imprimeDicionario():

    dicionario =    {
                        'jaspion':'power rangers',
                        'call of duty':'battlefield',
                        'eliana':'xuxa meneghel'
                    }
    for chave,valor in dicionario.items():
        print("Chave: %30s| Valor: %s " % (chave, valor))

def adicionaDicionario():

    dicionario =    {
                        'jaspion':'power rangers',
                        'call of duty':'battlefield',
                        'eliana':'xuxa meneghel'
                    }
    dicionario ['ratinho'] = 'gugu'
    for chave,valor in dicionario.items():
        print("Chave: %30s| Valor: %s " % (chave, valor))

def numerosDicionario():

    dicionario =    {
                        'monstros sa': 'mike wazowski',
                        'mundiais do palmeiras': [-1,0],
                        'galinha pintadinha': 'galo carijo'
                    }
    for chave,valor in dicionario.items():
        print("Chave: %30s| Valor(es): %s " % (chave, valor))

def imprimeLista():

    x = 1
    lista = [
            '@iagow', 
            ('maria', 'jose'), 
            {'harry':'potter','percy':'jackson'}, 
            3.14
            ]
    for elemento in lista:
        print("Elemento %d: {} ".format(elemento) % x)
        x+=1

def imprimeFrase():

    frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

    print(frase[0:18])


#Exercicio 1
print("Exercicio 1:")
imprime1a10()

#Exercicio 2
print("\nExercicio 2")
lista5objetos()

#Exercicio 3
print("\nExercicio 3")
concatenaString()

#Exercicio 4
print("\nExercicio 4")
contaTupla()

#Exercicio 5
print("\nExercicio 5")
dicionarioVazio()

#Exercicio 6
print("\nExercicio 6")
imprimeDicionario()

#Exercicio 7
print("\nExercicio 7")
adicionaDicionario()

#Exercicio 8
print("\nExercicio 8")
numerosDicionario()

#Exercicio 9
print("\nExercicio 9")
imprimeLista()

#Exercicio 10
print("\nExercicio 10")
imprimeFrase()
