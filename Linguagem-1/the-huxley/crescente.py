'''
Descrição
Receba dois números inteiros e os imprima em ordem crescente.

Formato de entrada

Dois números inteiros separados por um espaço em branco.

Formato de saída

Dois números inteiros separados por um espaço em branco.
'''

x,y = input().split()
if x>y:
    print(y,x)
else:
    print(x,y)