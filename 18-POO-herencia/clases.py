# Si una clase hereda de otra, al declarar la clase se pone entre ()
# Ejemplo: Informatico hereda de persona

class Persona:
    nombre = "Ander"
    apellidos = "Alvarez"
    altura = 177
    edad = 25

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return f"Hola, soy {self.nombre}"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):
    
    # Constructor
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

class TecnicoRedes(Informatico):

    def __init__(self):
        super.__init__()