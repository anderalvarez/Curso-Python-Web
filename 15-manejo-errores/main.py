# Capturar excepciones y manejar errores en el codigo
"""
try:
    nombre = input("Introduce tu nombre: ")
    print(nombre)
except:
    print('Ha ocurrido un error')
else:
    print('Todo ha ido bien') # Un else al except
finally: # Detectar cuando ha acabado el try/except/else
    print('Fin de la interacción')
"""


# Multiples Excepciones
try:
    numero = input('Numero para elevarlo al cuadrado: ')
    print("El cuadrado del numero es: " +str(numero*numero))
except Exception as e: # Almacenamos la excepción en una variable e
    print("Ha ocurrido un error", type(e).__name__)
"""
except TypeError:
    print("Debes convertir tus cadenas a entero en el codigo")
except ValueError:
    print("Debes introducir un número")
"""
# Excepciones personalizadas o lanzar excepciones

nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

if edad < 5 or edad > 110:
    # Con Raise se lanza una excepcion e indicas de que tipo quieres que sea
    raise ValueError("La edad no es correcta") 
elif len(nombre) <= 1:
    raise ValueError
else:
    print("Ha ido todo bien")
