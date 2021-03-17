"""
Programa que compruebe si una variable esta vacia y si lo está rellenarla
"""

variable = ""

if(len(variable) == 0):
    variable = input("La variable está vacia, introduce su valor: ")
else:
    print(f"La variable tiene el valor: {variable}")