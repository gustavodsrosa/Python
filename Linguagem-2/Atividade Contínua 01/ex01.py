'''
1) Escreva uma função com o nome pertence, que recebe 
como argumentos de entrada uma tupla e um item e 
retorna True, se o item estiver armazenado na tupla,
e False, caso contrário.
'''
def pertence(tupla, cont):
    return cont in tupla

tupla = (7, 8, 9)
print(pertence(tupla, 3))
print(pertence(tupla, 9))





