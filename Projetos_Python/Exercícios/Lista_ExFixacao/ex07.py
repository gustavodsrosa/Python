'''
7 - Faça um algoritmo para ler 15 números e armazenar em um vetor. Após a leitura total dos
15 números, o algoritmo deve escrever esses 15 números lidos na ordem inversa da qual foi
declarado.
'''

vetor = []

for i in range(15):
    n = input("Valor para a lista: ")
    vetor.append(n)

vetor.reverse()

print(vetor)