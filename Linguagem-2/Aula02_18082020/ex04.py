'''
Faça um programa que simule um lançamento de dados. O programa deve sortear 10 números
aleátorios (de 1 a 6) e armazenar esses números em uma lista.
Na sequência, informe quantas vezes cada número foi sorteado.
Exemplo:
Suponha que a lista com os números sorteados seja: 
[3, 1, 5, 3, 5, 4, 5, 5, 3, 1].
Para esta lista, o programa deve exibir:
Número 1 foi sorteado 2 vezes
Número 2 foi sorteado 0 vezes
Número 3 foi sorteado 3 vezes
Número 4 foi sorteado 1 vezes
Número 5 foi sorteado 4 vezes
Número 6 foi sorteado 0 vezes
'''
import random

# Lista base (formação dos dados)
base = []
for i in range(6):
    n = random.randint(1,6)
    base.append(n)
print('Lista base:', base)

# Definindo quantas vezes foi sorteado.

for i in range(len(base)):
    if base[i]  == 1:
        base.append(base[i])
        i+=1
print('O númer0 1 foi sorteado', i ,'vezes')