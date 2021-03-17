"""
Introduce un numero y luego el x% que quieres obtener
"""

numero = int(input("Introduce el numero: "))
porcentaje = int(input("Introduce el porcentaje: "))

resultado = str(numero * porcentaje / 100)

print(f"El {porcentaje}% de {numero} es {resultado}")