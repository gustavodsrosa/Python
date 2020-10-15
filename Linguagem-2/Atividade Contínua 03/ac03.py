class Pedido:
    def __init__(self, cliente, altura_placa, largura_placa, frase, cor_placa, valor, cor_letra, numero_letras):
        self.cliente = cliente
        self.altura_placa = altura_placa
        self.largura_placa = largura_placa
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147
        self.__valor_fixo_letra = 0.35
        self.__valor = valor
        self.numero_letras = numero_letras
    
    def get_valor(self):
        self.area = self.altura_placa * self.largura_placa
        self.custo_material = self.area * self.__valor_fixo_material
        self.custo_desenho = self.numero_letras * self.__valor_fixo_letra
        self.valor = self.custo_material + self.custo_desenho

    def emitir_recibo(self):
        print('Cliente:', self.cliente.nome)
        print('Telefone:', self.cliente.telefone)
        print('Largura da placa:', self.largura_placa)
        print('Altura da placa:', self.altura_placa)
        print('Frase:', self.frase)
        print('Quantidade de letras:', self.numero_letras)
        print('Valor:', self.valor)

class Historico:
    def __init__(self):
        self.pedidos = []
    
    def inserir_pedido(self):
        self.inserir_pedido.append(self.pedidos)
    
    def calcular_faturamento(self):
        somando = self.sum(self.pedidos)
        return somando


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


def separador():
    separador = '-=' * 30
    print(separador)


endereco = Endereco('Avenida Otacílio Negrão de Lima', 423, 32, "Pampulha", 'Belo Horizonte', 'MG', "31365-450")
cliente = Cliente('Paulo', '(31)5555-5555', endereco)
pedido = Pedido(cliente, 5, 4, "Reservado para Garagem", 'Amarela', 43, "Azul", 5)
pedido.get_valor()
pedido.emitir_recibo()
separador()
endereco1 = Endereco('Rodovia Castello Branco', 35, 77, "Remédios", 'São Paulo', 'SP', "00000-000")
cliente1 = Cliente('Antônio', '(11)3333-5555', endereco1)
pedido1 = Pedido(cliente1, 6, 7, "Cartas aqui", 'Amarela', 22, "Azul", 7)
pedido1.get_valor()
pedido1.emitir_recibo()
historico = Historico()
historico.inserir_pedido(pedido)
historico.inserir_pedido(pedido1)
historico.calcular_faturamento()
print(historico.calcular_faturamento())
