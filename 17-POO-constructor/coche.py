class Coche:

    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Para atributos privados hay que poner 2 barra bajas delante
    __propiedadPrivada = "Soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def setColor(self, color):
        self.color =  color

    def getColor(self):
        return self.color

    def setMarca(self, marca):
        self.marca =  marca

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo =  modelo

    def getModelo(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad =  velocidad

    def getVelocidad(self):
        return self.velocidad   

    def setCaballaje(self, caballaje):
        self.caballaje =  caballaje

    def getCaballaje(self):
        return self.caballaje

    def setPlazas(self, plazas):
        self.plazas =  plazas

    def getPlazas(self):
        return self.plazas

    def getPrivado(self):
        return self.__propiedadPrivada

    def getInfo(self):
        info = "Color -> " + self.getColor()
        info += "\nMarca -> " + self.getMarca()
        info += "\nModelo -> " + self.getModelo()
        info += "\nVelocidad -> " + str(self.getVelocidad())

        return info


    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1