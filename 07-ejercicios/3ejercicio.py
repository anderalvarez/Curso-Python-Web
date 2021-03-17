"""
Programa que muestre los cuadrados de los primeros 60 primeros numeros
"""

print("CON FOR:")

contador = 1
for contador in range(1, 61):
    print(contador*contador)


print("CON WHILE")

contador = 1
while contador <= 60:
    print(contador*contador)
    contador = contador + 1