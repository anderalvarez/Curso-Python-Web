numero = 3

def miNum():
    global numero2 # Convertir variable en global
    numero2 = 4

miNum()
print(numero)
print(numero2)