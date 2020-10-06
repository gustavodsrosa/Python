class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__rg = rg  # Atributo privado
        self.__cpf = cpf  # Atributo privado

    # Retorna o valor do self.__cpf
    def get_cpf(self):
        return self.__cpf

    # Retorna o valor do self.__rg
    def get_rg(self):
        return self.__rg

    # Altera o valor do self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf

    # Altera o valor do self.__rg
    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("João", 25, 1111111111, 999999)
pessoa1.nome = "João Paulo"
pessoa1.idade = 26
pessoa1.set_cpf(222222222)
print('CPF:', pessoa1.get_cpf())  # ERRO
