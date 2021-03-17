from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 120, 200, 4)
print(carro.getInfo())

# Detectar el tipado de un objeto
if type(carro) == Coche:
    print("Es un objeto de tipo Coche")
else:
    print("No es un coche")