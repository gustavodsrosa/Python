class Funcionario:
    nome = None
    salario = 0

    def aumentar_salario(self, salario, percentual):
        self.novosalario = salario * (1+(percentual/100))
    def mostrar(self):
        print(self.novosalario)

exibindo = Funcionario()
exibindo.aumentar_salario(7000.00, 5)
exibindo.mostrar()