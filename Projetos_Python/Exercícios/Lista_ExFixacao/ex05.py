'''
5 - Escreva um algoritmo que imprima a tabuada (de 1 a 10) para os números de
1 a 10.
Exemplo: tabuada do 1, tabuada do 2, etc... Dica: utilize um laço dentro do
outro
'''

for a in range(10):
    for b in range(10):
        print(f"{a+1} * {b+1} = {(a+1)*(b+1)}")
    print('=-' * 15)
