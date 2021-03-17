"""
Programa que tenga una lista de 8 numeros enteros y haga:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento
"""

lista = [1,2,3,4,5,6,7,8]

# Punto 1
def mostrarLista(lista):
    string = ""
    for elemento in lista:
        string = string + str(elemento) + ", "
    return string

print(mostrarLista(lista))
lista.sort()
print(mostrarLista(lista))
print(len(lista))

elemento = int(input("Introduce el numero a buscar: "))
encontrado = elemento in lista
if elemento:
    print(f"{elemento} se encuentra en la posicion {lista.index(elemento)}")
else:
    print(f"{elemento} no se encuentra en la lista")

