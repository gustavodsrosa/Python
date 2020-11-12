class Pessoa:
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.nome.append(disciplina)


class Funcionario(Pessoa):
    def __init__(self, nome, fone, cpf, salario):
        super().__init__(nome, fone, cpf)
        self.salario = salario


class Disciplina:
    def __init__(self, nome):
        self.nome = nome


class Professor(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super(endereco).__init__(nome, fone, cpf, salario, endereco)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir_disciplina(self, disciplina):
        self.disciplina.nome.append(disciplina)


class Tecnico(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super(endereco).__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo


# Instanciamento do objeto
disciplina1 = Disciplina('Programação')
disciplina2 = Disciplina('Banco de Dados')
professor1 = Professor('João', 'Rua Silva, 456', '(11)9999-9998', '88888888', 2000, 'Mestrado')
aluno1 = Aluno('Maria', 'Avenida São Francisco, 239', '(11)999887777', '5555555')
tecnico1 = Tecnico('Pedro', 'Rua Rocha, 77', '(11)987654321', '285874', 1500, 'Técnico')
aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)

print('Disciplinas relacionadas ao aluno: ')
for d in aluno1.disciplina:
    print(d.nome)

print('Disciplinas associadas ao professor: ')
for d in professor1.disciplina:
    print(d.nome)

