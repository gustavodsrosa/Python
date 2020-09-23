'''
- Definição da Classe Cachoro:
- Atributos: nome, peso, idade
- Metodo: Latir, Andar
'''
class Cachorro:
    nome = None
    peso = None
    idade = None

    def latir(self):
        print("O cachorro latiu")

    def andar(self):
        print("O cachorrou andou")

#instanciamento do objeto
meu_cachorro = Cachorro() 
meu_cachorro.nome = "Rex"
meu_cachorro.peso = 3.5
meu_cachorro.idade = 2
print("O nome do meu cachorro é: " + meu_cachorro.nome)
meu_cachorro.latir()
meu_cachorro.andar()