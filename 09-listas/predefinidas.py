# Ordenar lista
numeros = list((1,2,3,9,7,54,3))
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
numeros.append(6)

# Añadir elemento en una posicion
numeros.insert(0, 33)
print(numeros)

# Eliminar elementos
numeros.pop(4)

# Dar la vuelta a una lista
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
encontrado = 5 in numeros
print(encontrado)

# Contar elementos
longitud = len(numeros)
print(longitud)

# Cuantas veces aparece un elemento
vecesQueSeRepiteEl33 = numeros.count(33)
print(vecesQueSeRepiteEl33)
numeros.append(33)
vecesQueSeRepiteEl33 = numeros.count(33)
print(vecesQueSeRepiteEl33)

# Conseguir el indice
i = numeros.index(9)

# Unir listas
lista2 = ["Pepe", "Papa"]
numeros.extend(lista2)
print(numeros)