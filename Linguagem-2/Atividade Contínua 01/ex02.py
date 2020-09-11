'''
Escreva uma função chamada substitui que recebe como 
argumentos de entrada uma lista e dois itens (velho 
e novo) e retorna uma lista onde todas as ocorrências 
do item velho são substituídas pelo item novo.
'''

lista_atual = [1, 2, 3, 2, 4]
def substituir (lista_atual, antigo, mudado):
    for i in range (len(lista_atual)):
        if antigo == lista_atual[i]:
            lista_atual[i] = mudado
    return lista_atual

print(substituir(lista_atual, 2, 99))
print(substituir(lista_atual, 3, "abc"))