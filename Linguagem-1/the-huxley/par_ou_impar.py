'''
Descrição
Faça um programa que recebe um número inteiro e exibe 
uma mensagem indicando se ele é par ou ímpar 
(use o operador % para obter o resto de uma divisão inteira).

Formato de entrada

Um número inteiro.

Formato de saída

Uma mensagem "par" (minúsculo), caso o número seja par, 
ou "impar" (minúsculo e sem acento), caso o número seja ímpar.
'''

x = int(input())
if x%2==0:
    print('par')
else:  
    print('impar')
