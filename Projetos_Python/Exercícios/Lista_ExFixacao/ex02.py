'''
2 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
. até 20 litros, desconto de 3% por litro Álcool
. acima de 20 litros, desconto de 5% por litro
Gasolina:
. até 20 litros, desconto de 4% por litro Gasolina
. acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos e o tipo de
combustível (codificadoda seguinte forma: A-álcool, G-gasolina), calcule e
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
da gasolina é R$ 5,30 e o preço do litro do álcool é R$ 4,90.
Dica: utilize funções/métodos para otimizar o algorítimo.
'''


def calcular_preco(qtd, preco):
    return qtd * preco


preco = 0
qtd = float(input("Litros: "))
tipo = str(input("Tipo: (A) ou (G)? "))

if tipo == "A":
    preco = 4.90
    print(calcular_preco(preco, qtd))
elif tipo == "G":
    preco = 5.30
    print(calcular_preco(preco, qtd))


