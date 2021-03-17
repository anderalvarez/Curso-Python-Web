from tkinter import *

# Crear ventana raiz
ventana = Tk()

# Parametros de tamano por defecto
ventana.geometry("1000x600")

# Bloquear el tamano de la ventana
ventana.resizable(0,0) # Anchura y altura (1,0) deja dimensionar el ancho pero no el alto

# Icono de la ventana (Tiene que ser .ico)
ventana.iconbitmap("./21-tkinder/imagenes/logotipo.ico")

# Titulo de la ventana
ventana.title("ESTE ES EL TITULO DE LA VENTANA")
# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()

