# Dentro de python viene un gestor de BB.DD llamado SQLite (Usamos sqlite3)

import sqlite3

# Conexion
conexion = sqlite3.connect('Pruebas.db')

# Crear Cursor (Permite generar consultas)
cursor = conexion.cursor()

# Crear Tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INT(255)
    )
""")

"""
OTRA MANERA:

    cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "titulo VARCHAR(255), " +
    "descripcion TEXT, " +
    "precio INT(255)"+
    ")")
"""


# Guardar Cambios
conexion.commit()

# Insertar Datos en la tabla
"""
cursor.execute("INSERT INTO productos VALUES(null, 'Primer Producto', 'Descripcion del primer Producto', 33)")
conexion.commit()
"""

# Borrar Registros
cursor.execute("DELETE FROM productos") #Borra todos
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ("Ordenador", "Portatil", 700),
    ("Telefono", "Movil", 300),
    ("Placa base", "Pc Comp", 80),
    ("iPad", "Tablet", 400)
]
cursor.executemany("INSERT INTO productos VALUES (null ,?,?,?)", productos)
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall() # Obtener todos los registros

for producto in productos:
    print("-------------------------")
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])

"""
producto = cursor.fetchone() # Obtiene el primer registro
"""

# Cerrar Conexion
conexion.close()