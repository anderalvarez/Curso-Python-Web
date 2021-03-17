import mysql.connector

# Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# Cursor, permite ejecutar consultas
cursor = database.cursor(buffered=True) 
# Esto de buffered true es para cuando usemos mucho el cursor a veces se queda
# basura en su cache y casca.

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)

# CREAR TABLA
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# Insertar uno
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18000)")
database.commit()

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 200),
    ('Mercedes', 'Clase C', 35000)
]

# Insertar varios
cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()

# Obtener datos de la tabla
cursor.execute("SELECT * FROM vehiculos") 
# SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'

result = cursor.fetchall()
# cursor.fecthone() Coge solo el primero
for coche in result:
    print(coche)

# Borrar de una BBDD
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
database.commit()

# Ver Numero de registros del cursor
print(cursor.rowcount, " <- Numero de registros borrados")

# Actualizar marca Ibiza a Leon
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()
print(cursor.rowcount, " <- Numero de registros actualizados")