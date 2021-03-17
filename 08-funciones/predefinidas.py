# Detectar el tipado
nombre = "Ander"
comprobar = isinstance(nombre, str) # Comprueba el tipo de dato TRUE/FALSE

if comprobar:
    print("Es un String")
else:
    print("No lo es")

# Limpiar espacios string.strip()
frase = "     PROBANDO     "
print(frase)
fraseSinEspacio = frase.strip() 
print(fraseSinEspacio)

#Eliminar Variables
year = 2020
print(year)
del(year)
# print(year)


# Encontrar posicion en el string string.find(loquequieresencontrar)
# Si hay varias devuelve la que primero encuentre
frase = "Sic Mundus Creatus Est es una organización de viajes en el tiempo"
posicion = frase.find("tiempo") # Cuanta a partir de 0, no de 1
print(posicion)

# Reemplazar palabras de un string
nueva_frase = frase.replace("Sic Mundus Creatus Est", "La lonja")
print(nueva_frase)

# Mayusculas y Minusculas
nombreMinusculas = nombre.lower()
print(nombreMinusculas)

nombreMayusculas = nombre.upper()
print(nombreMayusculas)