# Exercício 2

try:
    lista = []
    # Usuário insere o nome de cinco pessoas
    for i in range(5):
        x = input('Digite o nome de uma pessoa: ')
        lista.append(x)
    print(lista)

    def position():
        a = int(input('Posição: '))
        print(lista[a])
except IndexError:
    print('Não tem na lista')
finally:
    position()



