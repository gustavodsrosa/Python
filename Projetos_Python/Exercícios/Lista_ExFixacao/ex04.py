'''
4 - Faça um programa que leia 10 valores digitados pelo usuário e no final, 
escreva o maior e o menor valor lido.
'''

lista = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

print()
print(f"Maior valor da lista: {max(lista)}")
print(f"Menor valor da lista: {min(lista)}")


