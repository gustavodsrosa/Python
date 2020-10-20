class Animal:
    def __init__(self, nome):
        self.nome = nome

    def talk(self):
        return "..."


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def talk(self):
        return "Miau!"


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def talk(self):
        return "Au Au"


def teste(animal):
    print(animal.talk())


def separador():
    separador = 0
    separador = '=-' * 30
    print(separador)


# Step 1
cat = Gato('Mefistofeles')
dog = Cachorro('Laika')
print(cat.talk())
print(dog.talk())

separador()

# Step 2
cat = Gato("Missy")
dog = Cachorro('Mefistofeles')
mouse = Animal('Rato')


animais = [cat, dog, mouse]

for i in animais:
    print(i.nome, ':', i.talk())


separador()

# Step 3
cat = Gato('cat')
dog = Cachorro('dog')
capivara = Animal('capivara')
teste(cat)
teste(dog)
teste(capivara)
