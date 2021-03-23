from tkinter import *
from tkinter import messagebox 

def sumar():
    resultado.set(float(numero1.get()) + float(numero2.get()))


def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))

def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))


ventana = Tk()
ventana.config(
    bd=25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

ventana.title("Calculadora")

Label(ventana, text="Numero1: ").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Numero2: ").pack()
Entry(ventana, textvariable=numero2).pack()

Button(ventana, text="Sumar", command=sumar).pack(side="left")
Button(ventana, text="Restar", command=restar).pack(side="left")
Button(ventana, text="Multiplicar", command=multiplicar).pack(side="left")
Button(ventana, text="Dividir", command=dividir).pack(side="left")

Label(ventana, textvariable=resultado).pack(side="bottom")

ventana.mainloop()