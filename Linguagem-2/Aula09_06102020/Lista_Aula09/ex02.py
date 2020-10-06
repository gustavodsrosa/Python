class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero


# Filme 1
filmes = []
dados = Filme("Titanic", "Drama")
dados.titulo = "O poderoso chefão"
dados.genero = "Máfia"
dados.set_titulo("O poderoso chefão")
dados.set_genero("Máfia")
dados.get_titulo()
dados.get_genero()
filmes.append(dados.get_titulo())
filmes.append(dados.get_genero())

# Filme 2
dados = Filme("Titanic", "Drama")
dados.titulo = "Luzes da Cidade"
dados.genero = "Romance"
dados.set_titulo("Luzes da Cidade")
dados.set_genero("Romance")
dados.get_titulo()
dados.get_genero()
filmes.append(dados.get_titulo())
filmes.append(dados.get_genero())

# Filme 3
dados = Filme("Titanic", "Drama")
dados.titulo = "Cassino"
dados.genero = "Máfia"
dados.set_titulo("Cassino")
dados.set_genero("Máfia")
dados.get_titulo()
dados.get_genero()
filmes.append(dados.get_titulo())
filmes.append(dados.get_genero())

# Exibindo a lista final
print(filmes)