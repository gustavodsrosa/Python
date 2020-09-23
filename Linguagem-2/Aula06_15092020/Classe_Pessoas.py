'''
Uma classe que permite cadastrar pessoas
- Atribuots: nome, email e telefone.
- Métodos: Um método deve exibir os dados desta pessoa.
'''
class Pessoa:
    nome = None
    email = None
    telefone = None

    def exibir_dados(self):
        print("Nome: " + self.nome)
        print("E-mail: " + self.email)
        print("Telefone: " + self.telefone)

victor = Pessoa()
victor.nome = "victor"
victor.email = "victorinac@gmail.com"
victor.telefone = "11-999999999"
victor.exibir_dados()
