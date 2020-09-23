class Triangulo:
    lado_a = 0
    lado_b = 0
    lado_c = 0
    resultado = 0

    def calcular_perimetro(self, lado_a, lado_b, lado_c):
        self.resultado = lado_a + lado_b + lado_c

    def exibir(self):
        print(self.resultado)

mostrar = Triangulo()

mostrar.calcular_perimetro(4, 5, 10)
mostrar.exibir()
