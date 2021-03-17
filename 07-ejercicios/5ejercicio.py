"""
Programa que muestre todos los numeros entre 2 que el usuario introduza
"""

inicio = int(input("Introduce el primer numero: "))
final = int(input("Introduce el segundo numero: "))

while inicio <= final:
    print(inicio)
    inicio = inicio + 1
    