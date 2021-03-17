from io import open # Manejo de ficheros
import pathlib # Tema de rutas
import shutil # Renombrar / Mover
import os #Para eliminar

# Crear un archivo
archivo = open("fichero_texto.txt", "a+")
archivo.close()
# Ruta Absoluta
ruta = str(pathlib.Path().absolute()) + "/" + "fichero_texto2.txt"
archivo2 = open(ruta, "a+")

# Escribir
archivo2.write("Soy un texto escrito desde python \n")

# Cerrar Archivo
archivo2.close()

# ---------------------------------------------

# Abrirlo para lectura
ruta = str(pathlib.Path().absolute()) + "/" + "fichero_texto2.txt"
archivo2 = open(ruta, "r")

# Leer el contenido
"""
contenido = archivo2.read()
print(contenido)

He tenido que comentarlo para que funcione lo de readlines(), 
no funcionaba porque ya lo habia leido antes
"""

# Leer y guardar en una lista
lista = archivo2.readlines()
archivo2.close()
# print(lista)

for frase in lista:
    lista_frase = frase.split() # Para convertir cada frase en una lista
    print(lista_frase)
    print("- "+ frase)

# Copiar un archivo
"""
ruta_original = str(pathlib.Path().absolute()) + "/" + "fichero_texto2.txt"
ruta_destino = str(pathlib.Path().absolute()) + "/" + "fichero_texto3.txt"
shutil.copyfile(ruta_original, ruta_destino)
"""
# Mover / Renombrar
"""
ruta_original = str(pathlib.Path().absolute()) + "/" + "fichero_texto3.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/" + "fichero_texto3_Nuevo.txt"
shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar
"""
ruta_nueva = str(pathlib.Path().absolute()) + "/" + "fichero_texto3_Nuevo.txt"
os.remove(ruta_nueva)
"""

# Mostrar ruta absoluta
"""
print(os.path.abspath("./"))
"""

# Comprobar si existe
import os.path

ruta_comprobar = str(pathlib.Path().absolute()) + "/" + "fichero_texto2.txt"

if os.path.isfile():
    print("El fichero existe")
else:
    print("El fichero NO existe")

