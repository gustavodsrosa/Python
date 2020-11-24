'''
6 - Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e
armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir
a leitura de mais 1 nome qualquer de pessoa (para efetuar uma busca)
e depois escrever a mensagem ACHEI, se o nome estiver entre os 10
nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.
'''

lista = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

nome = int(input("Digite um valor para ser verificado na lista: "))

if nome in lista:
    print("ACHEI")
else:
    print("NÃO ACHEI")


