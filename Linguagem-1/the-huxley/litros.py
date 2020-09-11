'''
Faça um programa que exibe quantos litros de combustível 
são gastos por um carro em um dado percurso. 
Serão fornecidos pelo usuário a distância percorrida (em km) 
e a quantidade de litros gastos por km.

Formato de entrada

Na primeira linha haverá um número inteiro representando a 
distância que será percorrida; na linha seguinte haverá um 
número real representando a quantidade de litros gastos por km.

Formato de saída

Um valor real com duas casas decimais representando a 
quantidade de litros gastos para realizar o percurso.
'''

distancia = int(input())
litros = float(input())
gasto = distancia * litros
print('%.2f '% gasto)