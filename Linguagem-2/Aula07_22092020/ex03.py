class Televisao:
    canal = None
    volume = 0

    def aumentar_volume(self, volume):
        self.volume += 1

    def diminuir_volume(self, volume):
        self.volume -= 1
    
    def alterar_canal(self, canal):
        print(self.canal)

tv = Televisao()

tv.aumentar_volume()


