'''
Crie uma classe Produto que possua os atributos nome, preco e descricao.

Crie um método exibir_descricao que exibe a descrição do produto.

Crie duas classes filhas de Produto, a classe Mouse com o atributo tipo e a
classe Livro com o atributo autor.

Crie o método exibir_descricao nas classes filhas, que deve exibir a descrição
do produto e o atributo adicional que a classe tiver (“autor” no caso de livro
e “tipo” no caso de mouse)

No programa principal você deve simular a compra de vários mouses e livros, e
inserir todos eles em uma lista chamada carrinho.

Chame o método exibir_descricao para cada objeto do carrinho.
'''


class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibir_descricao(self):
        print(self.descricao)


class Mouse(Produto):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo

    def exibir_descricao(self):
        print(self.descricao)
        print(self.tipo)


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor

    def exibir_descricao(self):
        print(self.descricao)
        print(self.autor)


# carrinho de compra vazio
carrinho = []

# criar os Produtos
m1 = Mouse("Mouse 1", 20.0, "mouse tipo 1", "Optico USB")
m2 = Mouse("Mouse 2", 100.0, "mouse tipo gamer", "Optico Gamer")
livro1 = Livro("Nome do Livro 1", 30.0, "Livro de Auto Ajuda", "nome do autor")

# colocar os produtos no carrinho
carrinho.append(m1)
carrinho.append(m2)
carrinho.append(livro1)

# exibir descricao dos produtos
for p in carrinho:
    p.exibir_descricao()
