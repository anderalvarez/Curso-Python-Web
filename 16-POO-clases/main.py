class Coche:

    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad    

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color


        
miObjetoCoche = Coche()

miObjetoCoche.acelerar()
miObjetoCoche.acelerar()

print(miObjetoCoche.getVelocidad())


