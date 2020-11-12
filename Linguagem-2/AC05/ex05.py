class CarroCorrida:
    def __init__(self, numero, piloto, velocidade_maxima, velocidade_atual):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = velocidade_atual
        self.__ligado = False

    def get_ligado(self):
        self.__ligado = True
    
    def ligar(self):
        print('Ligado: ', True)
    
    def set_ligado(self):
        return self.__ligado
    
    def desligar(self):
        print('Ligado: ', self.__ligado)
    
    def acelerar(self):
        print('Acelerar: ', self.__velocidade_maxima - self.__velocidade_atual, 'km/h')

    def frear(velocidade):
        print('Velocidade: ', 0, 'km/h')


carro = CarroCorrida(44, 'Hamilton', 300, 250)
carro.ligar()
carro.desligar()
carro.acelerar()
carro.frear()

    

    

