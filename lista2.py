"""
Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro)
e depois faça uma chamada à função para listar os números

Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma
string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma
string

Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos,
adicione 2 elementos a lista e imprima a lista

Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de
elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada
com 4 elementos

Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada
soma. A expressão vai receber 2 números como parâmetro e retornar a soma deles

Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre
variável global e local

    total = 0
    def soma( arg1, arg2 ):
        total = arg1 + arg2
        print ("Dentro da função o total é: ", total)
        return total

    soma( 10, 20 )
    print ("Fora da função o total é: ", total)

Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius Crie uma
função anônima que converta cada temperatura para Fahrenheit Dica: para conseguir
realizar este exercício, você deve criar sua função lambda, dentro de uma função). Isso
permite aplicar sua função a cada elemento da lista. Como descobrir a fórmula matemática
que converte de Celsius para Fahrenheit? Pesquise!!!

    Celsius = [39.2, 36.5, 37.3, 37.8]
    Fahrenheit = map(coloque_aqui_sua_função_lambda)
    print (list(Fahrenheit))

Exercício 8. Crie um dicionário e liste todos os métodos e atributos do dicionário

"""

def listaPares():
    for i in range(1,21):
        if(i%2==0):
            print(i)

def stringMaiuscula(texto):
    return texto.upper()

def novaLista(lista):
    lista.append("jonas")
    lista.append("brothers")
    print(lista)

def argLista(arg, *lista):
    print(arg)
    for i in lista:
        print(i)


#Exercicio 1
print("Exercicio 1:")
listaPares()

#Exercicio 2
print("\nExercicio 2")
print(stringMaiuscula("jonas brothers"))

#Exercicio 3
lista=[1,2,3,6]
print("\nExercicio 3")
novaLista(lista)

#Exercicio 4
print("\nExercicio 4")
print("Chamada 1:")
argLista(365)
print("Chamada 2:")
argLista("jonas", "brothers", "capitão", "areia")

#Exercicio 5
print("\nExercicio 5")
soma = lambda x, y: x + y
print("Soma: %d" % soma(2,2))

#Exercicio 6
print("\nExercicio 6")
print("As variáveis globais funcionam de maneira linear para todo o código")
print("ainda que uma de mesmo nome seja mudada dentro de uma função,")
print("pois a variável que mora dentro de uma função permanece lá como local")

#Exercicio 7
print("\nExercicio 7")
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: 9.0/5.0*x + 32, Celsius) # aplica a função pra cada elemento da lista Celsius
print(list(Fahrenheit)) # imprime a lista mapeada Fahrenheit

#Exercicio 8
print("\nExercicio 8")
dicionario = {"jonas":"brothers", "miley": "cyrus"}
print(dir(dicionario)) # retorna os metodos de um objeto
