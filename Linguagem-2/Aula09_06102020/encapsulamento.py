class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__rg = rg  # Atributo privado
        self.__cpf = cpf  # Atributo privado

pessoa1 = Pessoa("João", 25, 1111111111, 999999)
pessoa1.nome = "João Paulo"
pessoa1.idade = 26
print(pessoa1.nome)
print(pessoa1.__cpf)  # ERRO