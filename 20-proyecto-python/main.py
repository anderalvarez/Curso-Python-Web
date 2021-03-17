"""
Proyecto Python y MySQL
- Abrir asistente
- Login o registro
- Crear Usuario
- Crean Nota
"""

import usuarios.acciones as ua

print("""
Acciones Disponibles:
- Registro
- Login
""")

accion = input("Que quieres hacer: ").upper()
hazEl = ua.Acciones()

if accion == "REGISTRO":
    hazEl.registro()

elif accion == "LOGIN":
    hazEl.login()
