'''
Escreva um programa que solicite ao usuário seu nome
e sua idade. Depois que o usuário digitar o nome e a
idade, o programa deve exibir na tela duas mensagens:
uma com o nome e outra com a idade do usuário.
Suponha que o usuário seja o Pedro e tenha 32 anos.
Assim, seu programa deve exibir as mensagens:

Seu nome é Pedro

Você tem 32 anos
'''

nome = input('Nome: ')
idade = input('Idade: ')

print('Seu nome é',nome)
print(' ')
print('Você tem', idade, 'anos')