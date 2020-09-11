# Preencher lista com nome de cinco de pessoas.
# Não deve permitir nomes repetidos.

lista = []
for i in range(5):
    repeticao = True
    while repeticao == True:
        try:
            nome = input('Digite o nome: ')
            if nome in lista:
                raise ValueError
            else:
                lista.append(nome)
        except ValueError:
            print('Erro: O nome já existe')
        except Exception:
            print('Erro')
        else:
            repeticao = False

print(lista)