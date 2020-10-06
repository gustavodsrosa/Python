class Episodio:
    
    def __init__(self, numero, titulo, duracao, diretor):
        self.numero = numero
        self.titulo = titulo
        self.duracao = duracao
        self.diretor = diretor
        self.atores = []
    
    def mostrar_episodio(self):
        print('Número do episódio: ' ,self.numero)
        print('Título do episódio: ' ,self.titulo)
        print("Duração do episódio: " ,self.duracao)
        print('Diretor: ', self.diretor)
    
    def lista_atores(self):
        self.atores.append(num)
        print('Número dos atores: ', self.atores)


class Temporada:

    def __init__(self, numero):
        self.numero = numero
        self.episodios = []

    def mostrar_temporada(self):
        print('Número da temporada: ', self.numero)
    
    def lista_episodios(self):
        self.episodios.append(num1)
        print('Número da temporada: ', self.episodios)
    
class Ator:

    def __init__(self, nome):
        self.nome = nome
    def mostrar_nome_ator(self):
        print('Ator: ', self.nome)


class Diretor:

    def __init__(self, nome):
        self.nome = nome
    def mostrar_nome_diretor(self):
        print('Diretor: ', self.nome)

class Serie:

    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero
        self.temporadas = []

    def mostrar_serie(self):
        print('Nome da série: ', self.nome)
        print('Gênero: ' ,self.genero)

    def lista_temporadas(self):
        self.temporadas.append(num2)
        print('Número da temporada: ', self.temporadas)

def separador():
    separador = '=-' * 30
    print(separador)

# Classe Episódio
episodio = Episodio(9, 'Viagem a Acapulco', 60, 'Roberto Gomes Bolaños')
episodio.mostrar_episodio()
num = 1
episodio.lista_atores()
separador()

# Classe Temporada
temporada = Temporada(7)
temporada.mostrar_temporada()
num1 = 5
temporada.lista_episodios()
separador()

# Classe Ator
ator = Ator('Charles Chaplin')
ator.mostrar_nome_ator()
separador()

# Classe Diretor
diretor = Diretor('Alfred Hitchcock')
diretor.mostrar_nome_diretor()
separador()

# Class Série
serie = Serie('Todo Mundo Odeia o Chris', 'Comédia')
serie.mostrar_serie()
num2 = 5
serie.lista_temporadas()
separador()


