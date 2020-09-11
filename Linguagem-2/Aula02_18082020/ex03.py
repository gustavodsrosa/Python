'''
Preencha uma lista com 10 números sorteados aleatóriamente. 
A partir desta lista, gere uma lista
com os números pares e outra lista com os números ímpares.
Exemplo:
Suponha que a lista com os números sorteados seja: 
[1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]
'''
import random

# Lista inicial (lista de sorteio)
base = []
for i in range(10):
    n = random.randint(1,50)
    base.append(n)
print('Lista base:', base)

# Definindo números pares
pares = []
for i in range(len(base)):
    if base[i] % 2 == 0:
        pares.append(base[i])
print('Pares:', pares)

# Definindo números ímpares
impares = []
for i in range(len(base)):
    if base[i] % 2 != 0:
        impares.append(base[i])
print('Ímpares:', impares)