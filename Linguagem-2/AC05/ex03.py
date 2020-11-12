# Exercício 3


class Carro:
    quantidade_combustivel = 0
    distancia = 0

    def adicionar_combustivel(self, quantidade_combustivel):
        self.adicionar_combustivel = quantidade_combustivel
        print('Quantidade de combustível: ', self.adicionar_combustivel)

    def obter_combustivel(self):
        print('Combustível atual: ', self.adicionar_combustivel-self.quantidade_combustivel)
    
    def andar(self, distancia):
        self.andar = distancia * 0.2
        print('Distância:', self.andar)


carro = Carro()
carro.adicionar_combustivel(200)
carro.obter_combustivel()
carro.andar(130)
