from tkinter import *

ventana = Tk()

ventana.title("Marcos")
ventana.geometry("500x500")

# Le especifico la ventana donde va a estar y su tamaño
marco = Frame(ventana, width=200, height=200)

# Como Tk, tiene un .config
marco.config(
    bg="red",
    bd=5,
    relief="solid"
)
marco.pack(side=RIGHT, anchor=NE)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="orange"
)
texto.pack()



# marco = Frame(ventana, width=200, height=200)
# marco.config(
#     bg="green",
#     bd=5,
#     relief="solid"
# )
# marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()