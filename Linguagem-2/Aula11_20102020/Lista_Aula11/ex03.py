from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def limpar(self):
        pass

    def consertar(self):
        pass


class Bicicleta(Veiculo):
    def limpar(self):
        print('A bicicleta foi limpa')

    def consertar(self):
        print('A bicicleta foi consertada')


class Automovel(Veiculo):
    def limpar(self):
        print('O automóvel foi limpo')

    def consertar(self):
        print('O automóvel foi consertado')

    def trocar_oleo(self):
        print('O óleo foi trocado')


bike = Bicicleta()
carro = Automovel()

bike.limpar()
bike.consertar()
carro.limpar()
carro.consertar()

carro.trocar_oleo()
