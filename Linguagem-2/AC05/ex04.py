class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus
    

class Pessoa(Emprego):
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        qtd = len(self.dependentes)
        porcentagem = self.emprego.bonus * qtd
        salario = self.emprego.salario * (self.emprego.salario*(porcentagem/100))
        return salario


# Instanciamento do objeto 
emprego = Emprego('Analista de TI', 'TI', 3000, 10)
pessoa = Pessoa('Gilmar', '(11)987654321', 'gilmar@rj.com.br', emprego) # Recebe atributos da classe emprego 

dependente1 = Pessoa('Luiz', None, None, None)
dependente2 = Pessoa('José', None, None, None)

pessoa.dependentes.append(dependente1)
pessoa.dependentes.append(dependente2)

print('O salário é de: ', pessoa.calcular_salario())

