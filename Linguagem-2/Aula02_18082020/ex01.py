'''
Exercício 01 Lista de Exercícios - Aula 18/08/2020 - Professor Victor - LP2

Preencha uma lista com 10 números digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a média dos números contidos na lista
d) todos os números menores do que a média calculada no item anterior
'''

print('Por favor, escreva um número de cada vez!')
lista = []
for cont in range(10):
    n = int(input())
    lista.append(n)

# o maior número da lista

print("O maior valor da lista é: ", max(lista))

# o menor número da lista

print("O menor valor da lista é: ", min(lista))

# a média dos números contidos na lista

soma = sum(lista)
media = soma/10
print('A média da lista é de: ', media)

# todos os números menores do que a média calculada no item anterior

lista2 = []
for i in range(len(lista)):
    if lista[i] < media:
        lista2.append(lista[i])
print('Os números menores que a média são:', lista2)