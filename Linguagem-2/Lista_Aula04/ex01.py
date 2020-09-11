'''
Nesta questão você deve identificar as partes 
problemáticas do código e reescrevê-lo utilizando
tratamento de exceções.
Ou seja, devem ser identificadas todas as exceções 
que podem ser geradas e, para cada uma, deve ser dado 
o tratamento adequado que, nesse exercício, significa 
alertar o usuário quanto ao problema.

Código: 
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
'''

try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    if y < 0 or x < 0:
        raise RuntimeError
    c = x/y
    print('O resultado é de:', c)
except RuntimeError:
    print('Erro: O número deve ser natural')
except ValueError:
    print('Erro: Digite um caractere adequado ou número natural')
except ZeroDivisionError:
    print('Erro: Não existe divisão por zero')
except Exception:
    print('Erro: Foi digitado algo de errado')
