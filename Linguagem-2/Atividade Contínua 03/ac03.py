class Pedido:
    def __init__(self, cliente, altura_placa, largura_placa, frase, cor_placa, cor_letra, valor_fixo_material, valor_fixo_letra, valor):
        self.cliente = cliente
        self.altura_placa = altura_placa
        self.largura_placa = largura_placa
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = valor_fixo_material
        self.__valor_fixo_letra = valor_fixo_letra
        self.__valor = valor
    
    def get_valor(self):
        # Cálculos
        
    def emitir_recibo(self):
        '''Cliente: Paulo
        Telefone: (11)99999-4565
        Largura da Placa: 3.0
        Altura da Placa: 1.0
        Frase: 50% de Desconto
        Quantidade de letras: 13
        Valor: 445.55'''


class Historico:
    def __init__(self, pedidos):
        self.pedidos = []
    
    def inserir_pedido(self, pedido):
        # Inclui na lista
    
    def calcular_faturamento(self):
        # Somatório dos pedidos


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

