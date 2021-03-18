from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Welcome")
""""texto tiene un parametro config el cual puedes indicar para darle formato a la fuente"""
texto.config(
    fg="white",
    bg="black",
    font=("Arial", 12)
    )
texto.pack()

texto = Label(ventana, text="To the Jungle")
# El movimiento del texto se indica dentro del pack
texto.pack(anchor=E)

texto = Label(ventana, text="GG NOOB")
# El movimiento del texto se indica dentro del pack
texto.pack(anchor=W)

ventana.mainloop()