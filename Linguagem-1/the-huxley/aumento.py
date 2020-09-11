'''
Descrição
Faça um programa que lê o salário atual de alguém e exibe o novo 
salário, que é o atual com 25% de aumento.

Formato de entrada

Um número real representando o salário atual.

Formato de saída

Um número real com duas casas decimais, representando o 
salário atual com o aumento.
'''
1
salario = float(input())
novo = (salario * 25/100) + salario
print('%.2f'% novo)