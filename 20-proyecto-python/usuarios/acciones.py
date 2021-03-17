import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("Has indicado registro\n")
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        password = input("Introduce tu contrasena: ")
        email = input("Introduce tu email: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        print(registro)

        if registro[0]>=1:
            print(f"Hola {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print('No te has registrado')

    def login(self):
        print("Has indicado login")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contrasena: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has logeado en el sistema con {login[3]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
        
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles
        - Crear Nota (c)
        - Mostrar Notas (m)
        - Eliminar nota (e)
        - salir (s)
        """)

        accion = input("Introduce la opcion: ")

        if accion == "e":
            print(accion)
        elif accion == "c":
            print(accion)

        elif accion == "m":
            print(accion)

        elif accion == "s":
            print(accion)
            exit()

        


        
    