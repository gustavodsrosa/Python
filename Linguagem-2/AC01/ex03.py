'''
Escreva uma função chamada posicoes_lista que recebe 
como argumentos de entrada uma lista e um item, e 
retorna uma lista contendo todas as posições em que 
o item aparece na lista.
'''
'''
3) Escreva uma função chamada posicoes_lista que recebe 
como argumentos de entrada uma lista e um item, e 
retorna uma lista contendo todas as posições em que 
o item aparece na lista.
'''
lista_base = ['a', 2, 'b', 'a', 'a'] # Denominação da lista base
lista_para_adicionar = []
qual_caractere_escolher = 'a'
def posicoes_lista(lista_para_adicionar, qual_caractere_escolher): # Definição da função
    for i in range(len(lista_base)):
        if qual_caractere_escolher == lista_base[i]:
            lista_para_adicionar.append(i)
    print(lista_para_adicionar) # Exibir

posicoes_lista(lista_para_adicionar, qual_caractere_escolher) # Chamada da função






