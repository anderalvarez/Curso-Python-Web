agenda =  {
    "nombre": "Ander",
    "apellido 1": "Alvarez",
    "apellido 2": "Fernandez"
}

print(agenda["apellido 1"])

# Lista con diccionario

contactos = [
    {
        "nombre": "Pepe",
        "apellido 1": "Pepa",
        "apellido 2": "Pepo"
    },
    {
        "nombre": "AA",
        "apellido 1": "AA",
        "apellido 2": "AA"
    },
    {
        "nombre": "GG",
        "apellido 1": "GG",
        "apellido 2": "GG"
    },
    {
        "nombre": "QQ",
        "apellido 1": "QQ",
        "apellido 2": "QQ"
    }
]

print(contactos[2]["apellido 2"])

for contacto in contactos:
    print(f"El nombre del contacto es: {contacto['nombre']}") 
    # CUIDADO, USAR ' en vez de ""