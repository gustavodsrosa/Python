''' DESENVOLVEDOR - Salário maior do que três mil: '''

import ac02
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 5000.00, "DESENVOLVEDOR"])
    assert funcionario == 4000
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Resultado obtido: ", funcionario)
    print("Resultado esperado:", 4000)

''' DESENVOLVEDOR - Salário igual três mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 3000, "DESENVOLVEDOR"])
    assert funcionario == 2400
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Resultado obtido: ", funcionario)
    print("Resultado esperado:", 2400)

''' DESENVOLVEDOR - Salário menor do que três mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 2000, "DESENVOLVEDOR"])
    assert funcionario == 1800
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Resultado obtido: ", funcionario)
    print("Resultado esperado:", 1800)

''' ANALISTA - Salário maior do que dois mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 2500, "ANALISTA"])
    assert funcionario == 1875
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 1875)


''' ANALISTA - Salário igual a dois mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 2000, "ANALISTA"])
    assert funcionario == 1500
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 1500)

''' ANALISTA - Salário menor do que dois mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 1500, "ANALISTA"])
    assert funcionario == 1275
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 1275)

''' GERENTE - Salário maior igual a cinco mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 5000, "GERENTE"])
    assert funcionario == 3500
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 3500)

''' GERENTE - Salário maior do que cinco mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 5500, "GERENTE"])
    assert funcionario == 3850
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 3850)

''' GERENTE - Salário menor do que cinco mil: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 3500, "GERENTE"])
    assert funcionario == 2800
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print("Valor obtido:", funcionario)
    print("Valor esperado:", 2800)

''' CARGO INEXISTENTE NA EMPRESA: '''
try:
    funcionario = ac02.salario(["Marcílio dos Santos", "marcilio@email.com", 3500, "ESTOQUE"])
    assert funcionario == 2800
    print("Correto!!")
except AssertionError:
    print("Erro!!")
    print(funcionario)
