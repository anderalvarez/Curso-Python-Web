nada = None # Es como el null
print(nada)
print(type(nada))

print("-----------------------------")

cadena = "Ander Álvarez Fernández"
print(cadena)
print(type(cadena))

print("-----------------------------")

entero = 33
print(entero)
print(type(entero))

print("-----------------------------")

flotante = 33.3
print(flotante)
print(type(flotante))

print("-----------------------------")

booleano = True
print(booleano)
print(type(booleano))

print("-----------------------------")

lista = [10,20,30,"100",200]
print(lista)
print(type(lista))

print("-----------------------------")

tupla = ("Ander", "Álvarez") #Lista que sus datos no cambian
print(tupla)
print(type(tupla))

print("-----------------------------")

diccionario = {
    "nombre": "Ander",
    "apellidos": "Álvarez"
} 
print(diccionario)
print(type(diccionario))

print("-----------------------------")

rango = range(9)
print(rango)
print(type(rango))

print("-----------------------------")

dato_byte = b"dato"
print(dato_byte)
print(type(dato_byte))


# CONVERTIR UN TIPO DE DATO A OTRO

texto = "44"
numero = 33

#print(texto + numero) 
# # Esto da un error

numeroStr = str(numero)
print(texto + numeroStr)

textoNum = int(texto)
suma = textoNum + numero

print(suma)