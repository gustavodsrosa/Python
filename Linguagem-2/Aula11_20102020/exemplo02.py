# Exemplo Classes Abstratas

from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_salario(self):
        return self.salario * 1.2


# Instanciamento do objeto
func = Funcionario('João', 1000)
print(func.calcular_salario())
