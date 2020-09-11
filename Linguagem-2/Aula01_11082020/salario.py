'''
Escreva um programa que leia o salário de um
funcionário e exiba na tela o valor do salário com um
reajuste de aumento, sendo que:

Caso o salário atual seja maior que R$ 2.000,00
receberá 7% de aumento.

Caso contrário, receberá 15% de aumento.
'''

salario = float(input('Escreva seu salário:'))

if salario > 2000:
    salario_final = salario * 1.07
else:
    salario_final = salario * 1.15

print("Seu salário é de: %.2f" % salario_final)

