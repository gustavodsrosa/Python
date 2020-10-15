class Livro:
    titulo = None
    autor = None
    quantidade_paginas = 0

    def abrirLivro(self):
        print('O título é: ' + self.titulo)
        print('O autor é: ' + self.autor)
        print('O número de páginas é de: ' + self.quantidade_paginas)

# Instanciamento do objeto
mostrando = Livro()
mostrando.titulo = 'Memórias Póstumas de Brás Cubas'
mostrando.autor = 'Machado de Assis'
mostrando.quantidade_paginas = '216'
mostrando.abrirLivro()

