from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):

    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 1.1)

 
# Instanciamentos

g = Gerente("João", 123, 2000)
a = Assistente("Ana", 333, 2000)
v = Vendedor("Maria", 456, 2000)

funcionario = [g, a, v]

for f in funcionario:
    print("Salario:", f.calcular_salario())
