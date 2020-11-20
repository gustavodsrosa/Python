'''
1 - Faça um programa que receba o nome e quatro notas de 10 alunos e armazene
essas notas em vetores. Calcule e mostre:
    A. A Média do aluno - Função
    B. A quantidade de Aprovados (Média >= 7)
    C. A quantidade de Reprovados (Méida < 7)
    D. A Média geral dos 10 alunos.
'''

nome_alunos = []
n1 = []
n2 = []
n3 = []
n4 = []
media = []
aprovados = []
reprovados = []
media_geral = []

for i in range(10):
    nome = str(input("Digite o nome do aluno(a): "))
    nome_alunos.append(nome)
    nota1 = float(input("Nota1: "))
    n1.append(nota1)
    nota2 = float(input("Nota2: "))
    n2.append(nota2)
    nota3 = float(input("Nota3: "))
    n3.append(nota3)
    nota4 = float(input("Nota4: "))
    n4.append(nota4)
    print()
    print(f'Você cadastrou até agora {i+1} alunos')
    print()

print(nome_alunos)
print(n1)
print(n2)
print(n3)
print(n4)

for c in range(0, 10):
    nome = nome_alunos[c]
    media_n = (n1[c] + n2[c] + n3[c] + n4[c])/4
    media.append(media_n)
    if media[c] >= 7:
        aprovados.append(media[c])
    else:
        reprovados.append(media[c])

print("Aprovados: ", len(aprovados))
print("Reprovados: ", len(reprovados))

med_inicial = media[0] + media[1] + media[2] + media[3] + media[4]
med_final = media[5] + media[6] + media[7] + media[8] + media[9]

med_geral = (med_inicial + med_final)/10
media_geral.append(med_geral)

print("Lista de Alunos: ", nome_alunos)
print("Lista de Notas: ", n1)
print("Lista de Notas: ", n2)
print("Lista de Notas: ", n3)
print("Lista de Notas: ", n4)
print("Aprovados: ", len(aprovados))
print("Reprovados: ", len(reprovados))
print("Média Geral: ", media_geral)
