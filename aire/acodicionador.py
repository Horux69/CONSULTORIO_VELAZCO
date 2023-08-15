class Acondicionador:
    def __init__(self, ubica):
        self.ubicacion = ubica
        self.estado = False
        self.temperatura = 16

    def encendido(self):
        self.estado =  not self.estado

    def aumentar(self):
        if self.temperatura < 30:
            self.temperatura += 1

    def disminuir(self):
        if self.temperatura > 16:
            self.temperatura -= 1

    def ponerTemp(self, temp):
        if temp > 16 and temp <30:
            self.temperatura = temp
        else:
            self.temperatura = 16

    def visualizar(self):
        print(f"Aire acondicionado unicado en: {self.ubicacion}")

        if self.estado:
            print(f"El estado es encendico")
        else:
            print(f"El estado es apagado")

        print(f"la temperatura es: {self.temperatura}")

    