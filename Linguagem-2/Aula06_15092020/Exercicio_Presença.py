'''
Faça o UML e o código orientado a objetos para o problema  mostrado a seguir:

Crie uma classe para efetuar cálculos matemáticos a partir de dois números digitados pelo usuário.
 Os métodos deverão ser soma, subtração, multiplicação e divisão.

Instancie um objeto para testar.

Envie um print do UML e o código fonte contendo a classe e o objeto.
'''

# Classe para fazer os cálculos
class fazerCalculo:
    # Variável que recebe os cálculos
    num1 = 0 

    # Variável que recebe os cálculos
    num2 = 0 

    # Variável que recebe o resultado
    resultado = 0 

    # Função soma
    def soma(self, num1, num2):
        self.resultado = num1 + num2

    # Função subtração
    def subtracao(self, num1, num2):
        self.resultado = num1 - num2

    # Função multiplicação
    def multiplicacao(self, num1, num2):
        self.resultado = num1 * num2
  
    #Função divisão
    def divisao(self, num1, num2):
        self.resultado = num1 / num2

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
