# Atividade presença Aula 08/09/2020

# Funções

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

def converte_para_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Importando as funções
import fahr_cels        # Converte de fahrenheit para celsius
import cels_fahr        # Converte de celsius para fahrenheit

# Teste de mesa
try:
    celsius = fahr_cels.converte_para_celsius(90) # Mudar número
    assert celsius >= 0
    print(celsius)
except AssertionError:
    print('Erro')
    print('Retorno', celsius)
    print('Esperado:', 30)

try:
    fahrenheit = cels_fahr.converte_para_fahrenheit(32) # Mudar número
    assert fahrenheit >= 0
    print(fahrenheit)
except AssertionError:
    print('Erro')
    print('Retorno', fahrenheit)
