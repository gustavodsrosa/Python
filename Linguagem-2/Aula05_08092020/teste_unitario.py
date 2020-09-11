import modulo

try:
    c = modulo.soma(10,20)
    assert c == 30
    print('Correto')
except AssertionError:
    print('Erro')
    print('Retorno', c)
    print('Esperado:', 30)
