# Criação da classe para fazer os cálculos
class Calculadora:

    # Método de construtor para definir as variáveis 
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Método que realiza a soma
    def soma(self):
        return self.a + self.b
    
    # Método que realiza a subtração
    def subtrai(self):
        return self.a - self.b
    
    # Método que realiza a multiplicação
    def multiplica(self):
        return self.a * self.b
    
    # Método que realiza a divisão
    def divide(self):
        return self.a / self.b

# Recebendo a variável a
a = 7

# Recebendo a variável b
b = 9

# Instanciamento do objeto
calcula = Calculadora(a,b)

# Retornando e exibindo o método de soma
calcula.soma()
print(calcula.soma())

# Retornando e exibindo o método de subtração
calcula.subtrai()
print(calcula.subtrai())

# Retornando e exibindo o método de multiplicação
calcula.multiplica()
print(calcula.multiplica())

# Retornando e exibindo o método de divisão
calcula.divide()
print(calcula.divide())