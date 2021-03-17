"""
Mostrar todos los numeros impares entre dos numeros
"""

inicio = int(input("Introduce el primer numero: "))
final = int(input("Introduce el segundo numero: "))

for i in range(inicio, final+1):
    if i%2 != 0:
        print(i)