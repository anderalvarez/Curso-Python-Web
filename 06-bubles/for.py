contador = 0

for contador in range(0, 5): #Del 0 al 4
    print(f"voy por el {contador}")


numero1 = 1
numero2 = 2
resultado = 0
for numero1 in range(1,12):
    for numero2 in range(1,12):
        resultado = numero1*numero2
        if resultado == 33:
            print("Has llegado al numero supremo")
            break
        print(resultado)