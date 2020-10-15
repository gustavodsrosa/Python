class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = Motor

    def exibir_dados(self):
        print('Ano:', self.ano)
        print('Preco:', self.preco)
        print('Motor:', self.motor)


class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        super().exibir_dados()
        print('Cor:', self.cor)
        print('Modelo:', self.modelo)


class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        super().exibir_dados()
        print('Comprimento:', self.comprimento)


motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, 'Branca', 'Gol')
caminhao = Caminhao(2015, 80000, motor2, 10)
carro.exibir_dados() 
caminhao.exibir_dados()

