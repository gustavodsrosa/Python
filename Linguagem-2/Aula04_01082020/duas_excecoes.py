try:
    a = int(input('Escolha o primeiro número: '))
    b = int(input('Escolha o segundo número: '))
    print(a/b)
except ZeroDivisionError:
    print('Não existe divisão por zero, escolha outro')
except ValueError:
    print('O tipo de caractere é incorreto, digite outro')
except Exception:
    print('Algo errado aconteceu na execução')
finally:
    print('Fim de programa')