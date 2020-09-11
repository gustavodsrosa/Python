'''
Escreva uma função que recebe como parâmetro um
número N e exibe todos os divisores desse número.
'''

def divisores():
    numero = int(input('Escreva seu número: '))

    for c in range(1, numero+1) :
        if numero % c == 0:
            print(c)

divisores()
