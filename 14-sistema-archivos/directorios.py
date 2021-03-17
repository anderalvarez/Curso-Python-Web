import os

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")


# Eliminar
os.rmdir("./mi_carpeta")

# Copiar carpeta
import shutil

ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_nueva"
shutil.copytree(ruta_original, ruta_nueva)

# Listar archivos de una carpeta
os.listdir(ruta_original)