# coding=utf-8

def salario(salario, aumento):
    aumento = salario*(aumento/100.0)
    salario += aumento
    print("Seu aumento foi de %.2f e seu novo salario é de %.2f" % (aumento, salario))
    
salario(1000,10)