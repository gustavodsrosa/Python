class Pessoa:
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    disciplina = []
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
    
    def incluir_disciplina(disciplina):
        disciplina.append(self.nome)


class 

