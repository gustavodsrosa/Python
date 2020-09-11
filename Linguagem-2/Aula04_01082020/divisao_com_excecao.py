try:
    a = int(input('Escolha o primeiro número: '))
    b = int(input('Escolha o segundo número: '))
    print(a/b)
except ZeroDivisionError:
    print('Não existe divisão por zero, escolha outro')

# Se o usuário digitar uma vez errado, contabiliza na próxima
while b == 0:
    b = int(input('Escolha o segundo número: '))
    print(a/b)