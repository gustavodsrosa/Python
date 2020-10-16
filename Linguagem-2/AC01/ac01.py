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

#----------------------------------------------------------------------

'''
2) Escreva uma função chamada substitui que recebe como 
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

#----------------------------------------------------------------

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

#--------------------------------------------------------------------------------------

'''
4) Suponha um dicionário onde a chave é o nome de um 
aluno e o valor uma lista de 3 notas.
Escreva uma função chamada aprovados que recebe 
como argumentos de entrada o dicionário e retorna 
uma lista com o nome dos alunos aprovados 
(um aluno é aprovado quando a média das suas notas
é maior ou igual a 6).
'''

# Dicionário
alunos = {'Augusto':[4.5, 7.0, 6.0],
          'Denise': [9.0, 8.5, 9.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0]}

# Configuração dos alunos na lista
lista_alunos = []
notas_dos_alunos = {}
def aprovados(alunos):
    for cont in range(4):
        nome_dos_alunos = input('Digite seu nome:')  
        n1 = float(input('Primeira Nota:'))
        n2 = float(input('Segunda Nota:'))
        n3 = float(input('Terceira Nota:'))          
        print('\n') # Quebra de linha a cada inserção de nota
        media_dos_alunos = (n1+n2+n3)/3 # Média dos alunos
        if media_dos_alunos >= 6:
            lista_alunos.append(nome_dos_alunos) # Adicionar nome dos alunos na lista de alunos
    print(lista_alunos) # exibir
    
aprovados(alunos) # chamada da função


