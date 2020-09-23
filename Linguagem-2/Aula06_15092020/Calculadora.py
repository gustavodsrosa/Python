'''
Uma classe que simula uma calculadora de 2 operações (somar e subtrair)
'''
class Calculadora:
    x = 0
    y = 0
    resultado = 0

    def somar(self, x, y):
        self.resultado = x + y

    def subtra(self, x, y):
        self.resultado = x - y

    def exibir_resultado(self):
        print(self.resultado)


calc = Calculadora()
calc.somar(10, 20)
calc.exibir_resultado()
calc.subtrair(100, 30)
calc.exibir_resultado()