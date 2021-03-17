"""
Escribir un script que muestre todos los numeros pares del 1 al 120
"""

contador = 1

for contador in range(1,121):
    if(contador%2==0):
        print(contador)