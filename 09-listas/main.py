# Listas son como arrays

peliculas = ["Matrix", "Matrix 2", "Matrix 3"]
print(peliculas)

series = list(("Como conocí a vuestra madre", "Los Simpsons", "Dos Hombres y Medio"))

# Indices
print(peliculas[1])
print(peliculas[-1]) # Con indice negativo empieza desde el final
print(series[0:2])

# Añadir list.append
series.append("Nueva serie")
print(series)

# Recorrer lista
for serie in series:
    print(f"{series.index(serie)}. {serie}")

# Listas Multidimensionales 
# Sin mas pone el mitico ejemplo de una agenda de contactos

