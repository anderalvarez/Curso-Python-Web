# En python no hace falta declarar el tipo de variable
texto = "Master en phython"
print(texto)

# Se puede machacar el tipo de variable
texto = 1
print(texto)

"""
    CONCATENAR VARIABLES
"""

nombre = "Ander"
apellidos = "Álvarez Fernández"

print(nombre + " " + apellidos)

# Otra forma es con f{}{}, la f{} se puede usar tambien en las variables
print(f"{nombre} {apellidos}")

# Otra forma es usando el metodo format String.format(parametros donde habia {})
print("Hola me llamo {} {}".format(nombre, apellidos)) 