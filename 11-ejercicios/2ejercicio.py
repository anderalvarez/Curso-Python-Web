"""
Escribir un programa que añada valores a una lista mientras su longitud sea menor a 120
PLUS: FOR y WHILE
"""

lista = []

## FOR
for numero in range(0, 120):
    elemento = input(f"Introduce el {numero} elemento de la lista: ")
    lista.append(elemento)

# WHILE
contador = 0
while contador < 120:
    elemento = input(f"Introduce el {numero} elemento de la lista: ")
    lista.append(elemento)
    contador = contador + 1