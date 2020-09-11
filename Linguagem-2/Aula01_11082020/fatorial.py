'''
Escreva uma função que recebe como parâmetro de
entrada um número N positivo, e retorna o fatorial de n.
'''

def fatorial():
    numero = int(input('Digite um número: '))
    i = 1 
    fatorial = 1  

    while i <= numero:
        fatorial = fatorial * i 
        i += 1

    print(fatorial)

fatorial() 