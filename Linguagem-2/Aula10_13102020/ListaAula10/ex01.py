class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome


class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        self.cnpj = cnpj
        super().__init__(identificador, nome)


class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        self.rg = rg
        self.cpf = cpf
        super().__init__(identificador, nome)


# Instanciamento do Objeto
pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")

print(pessoa1.identificador)        # 1
print(pessoa1.nome)                 # Nome da Pessoa

print(p_juridica.identificador)     # 2
print(p_juridica.nome)              # Nome da Pessoa Juridica
print(p_juridica.cnpj)              # 1111111111

print(p_fisica.identificador)       # 3
print(p_fisica.nome)                # Nome da Pessoa Fisica
print(p_fisica.rg)                  # 222222222
print(p_fisica.cpf)                 # 333333333
