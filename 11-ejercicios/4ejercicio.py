"""
Crear un programa con 4 variables, una lista, un string, un entero y un booleano
"""

def mostrarTipoDato(dato):
    tipo = type(dato)
    print(f"{dato} es de tipo {tipo}")

lista = []
string = ""
entero = 33
booleano = True

mostrarTipoDato(lista)
mostrarTipoDato(string)
mostrarTipoDato(entero)
mostrarTipoDato(booleano)