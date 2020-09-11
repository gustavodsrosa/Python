'''
Preencha uma lista com 20 números sorteados aleatóriamente 
(utilize a função randint do
módulo random para sortear os números).
'''

import random
lista = []
for i in range(20):
    n = random.randint(1,10000)
    lista.append(n)
print(lista)