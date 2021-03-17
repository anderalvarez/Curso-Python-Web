"""
Pedid dos numeros a un usuario y realizar sum/resta/mult/div
"""

numero1 = int(input("Introduce el numero 1: "))
numero2 = int(input("Introduce el numero 2: "))

suma = numero1+numero2
resta = numero1-numero2
multiplicacion = numero1*numero2
if(numero2 != 0):
    division = numero1/numero2
    print(f"La division es: {division}")
else:
    print("No se puede dividir entre 0")

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")