class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = 300000.0

class Novo(Imovel):
    def __init__(self, adicional, endereco, preco):
        super().__init__(endereco, preco)
        self.adicional = 25000.0

    def calcular_preco(self):
        print(self.adicional + self.preco)


class Velho(Imovel):
    def __init__(self, desconto, endereco, preco):
        super().__init__(endereco, preco)
        self.desconto = 35000.0
    def calcular_preco(self):
        print(self.preco - self.desconto)


imovel = Imovel('Rua Silva, 123', 300000.0)
imovel_novo = Novo('Rua Joaquim, 999', 250000.0, 20000.0)
imovel_velho = Velho('Av. Brasil, 777', 500000.0, 35000.0)
print(imovel.endereco)              # Rua Silva, 123
print('Preço:', imovel.preco)       # 300000.0
print(imovel_novo.endereco)         # Rua Joaquim, 999
print('Preço:', imovel_novo.preco)  # 250000.0
print('Preço atualizado:', imovel_novo.calcular_preco()) # 270000.0
print(imovel_velho.endereco) # Av. Brasil, 777
print('Preço', imovel_velho.preco) # 500000.0
print('Preço Atualizado:', imovel_velho.calcular_preco())