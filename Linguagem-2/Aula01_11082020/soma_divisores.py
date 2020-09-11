'''
Escreva uma função que recebe como parâmetro um
número N e retorna a soma de todos os divisores desse
número.
'''

def soma_divisores():
    numero = int(input('Escreva seu número: '))

    soma = 0
    for c in range(1, numero+1) :
        if numero % c == 0:
            soma += c
    print(soma)

soma_divisores()
