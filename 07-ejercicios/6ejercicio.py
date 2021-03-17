"""
Mostrar todas las tablas de multiplicar entre el 1 y el 10
"""

for i in range(1, 11):
    print(f"TABLA DE MULTIPLICAR DEL {i}")
    print("-------------------------------")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
        