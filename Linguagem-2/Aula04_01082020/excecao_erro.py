try:
    a = int(input('Informe um número natural: '))
    b = int(input('Informe um número natural: '))

    # Gerar exceção no erro
    if a < 0 or b < 0: 
        raise RuntimeError
    c = a/b
    if b > a:
        print("O resultado é de %.2f"% c)
    else:
        print('O resultado é de:', int(c))
except ZeroDivisionError:
    print('Erro. Não pode dividir por zero')
except ValueError:
    print('Erro. Número inválido')1
except NameError:
    print('Erro. Nome de variável inválido')
except RuntimeError:
    print('Erro. O número deve ser natural')
except Exception:
    print('Erro. Ocorreu um erro inesperado')
else:
    print('Programa utilizado com sucesso')
finally: 
    print('Até mais')