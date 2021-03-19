from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Titulo de la ventana"
        self.icon = "./21-tkinder/imagenes/logotipo.ico"
        self.size = "1000x600"
        self.resizable = True

    def cargar(self):
        # Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Parametros de tamano por defecto
        ventana.geometry(self.size)

        # Bloquear el tamano de la ventana
        if self.resizable == True:
            ventana.resizable(1,1) # Anchura y altura (1,0) deja dimensionar el ancho pero no el alto
        else:
            ventana.resizable(0,0)
        # Icono de la ventana (Tiene que ser .ico)
        ventana.iconbitmap(self.icon)

        # Titulo de la ventana
        ventana.title(self.title)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
    
    def mostar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()


# Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Texto añadido desde funcion")
programa.addTexto("Viva España")
programa.mostar()
