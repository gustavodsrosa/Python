class Emprego:
     
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus

class Pessoa:

    def __init__(self, nome, fone, email, emprego, dependentes):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = dependentes

    def calcular_salario(self):
        qtd = len(self.dependentes)
        porcentagem = self.emprego.bonus * qtd
        salario = self.emrepgo.salario * (self.emprego.salario*porcentagem/100)
        print(salario)


# Instanciamento do objeto 
emprego = Emprego('Analista de TI', 'TI', 3000, 10)
pessoa = Pessoa()

