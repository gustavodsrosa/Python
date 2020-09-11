'''
Dados três números em ponto flutuante queremos saber quantos 
deles estão acima da média aritmética.

Formato de entrada

Três números positivos, menores ou iguais a 10.0 e com 
dois decimais, no máximo.
Formato de saída

A quantidade dos que estão acima da média.
'''

a = float(input())
b = float(input())
c = float(input())
med = (a + b + c)/3
qtd = 0
if a > med:
    qtd = qtd + 1
if b > med:
    qtd = qtd + 1
if c > med:
    qtd = qtd + 1
print(qtd)
