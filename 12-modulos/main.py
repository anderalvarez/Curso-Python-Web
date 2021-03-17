import mimodulo

print(mimodulo.holaMundo("Ander"))
mimodulo.calculadora(33,33)

# Para importar una funcion unicamente:
"""
from mimodulo import nombreFuncion
"""

# Para llamarles sin tener que poner mimodulo.
"""
from mimodulo import *
"""

# Modulo de Fechas
import datetime

print(datetime.date.today()) # Sacar la fecha de hoy

fecha_completa = datetime.datetime.now()
print(fecha_completa)

print(fecha_completa.year)

# Personalizar la fecha
fecha_personalizada = fecha_completa.strftime("%d/%Y/%m, %S/%H/%M")
print(fecha_personalizada)


"""
MODULO DE MATEMÁTICAS
"""

import math