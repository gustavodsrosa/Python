'''
Suponha um dicionário onde a chave é o nome de um 
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
    for cont in range(5):
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




