'''
Uma classe que simula uma calculadora de 2 operações (somar e subtrair)
'''

# Classe para fazer os cálculos
class fazerCalculo:
    # Variável que recebe os cálculos
    x = 0 

    # Variável que recebe os cálculos
    y = 0 

    # Variável que recebe o resultado
    resultado = 0 

    # Função soma
    def soma(self, x, y):
        self.resultado = x + y

    # Função subtração
    def subtracao(self, x, y):
        self.resultado = x - y

    # Função multiplicação
    def multiplicacao(self, x, y):
        self.resultado = x * y
  
    #Função divisão
    def divisao(self, x, y):
        self.resultado = x / y

    # Função exibir
    def mostrar(self):
        print(self.resultado)


# Instanciando o objeto
calculadora = fazerCalculo()

# Retornando a função soma
calculadora.soma(10, 20)
calculadora.mostrar()

# Retornando a função subtração
calculadora.subtracao(10, 20)
calculadora.mostrar()

# Retornando a função multiplicação
calculadora.multiplicacao(10, 20)
calculadora.mostrar()

# Retornando a função divisão
calculadora.divisao(10, 20)
calculadora.mostrar()