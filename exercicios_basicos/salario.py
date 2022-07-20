# coding=utf-8

def aumento_salario(salario, aumento):
    aumento = salario*(aumento/100.0)
    salario += aumento
    print("Seu aumento foi de R$%.2f e seu novo salario é de R$%.2f" % (aumento, salario))

salario = float(input("Digite o valor do salario: "))
aumento = float(input("Digite a porcentagem do aumento: "))
aumento_salario(salario, aumento)
