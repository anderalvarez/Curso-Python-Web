def mifuncion(parametro1, parametro2 = None): #parametro2 = None es para que sea "Opcional", realmente se le asgina ahi el valor... Este tutorial apesta
    print(f"el parametro1 es {parametro1}")
    print(f"el parametro2 es {parametro2}")

mifuncion(1,4)
mifuncion(3,6)


# Funciones Lambda o anonimas
# Son funciones sencillas que se pueden definir en una linea de codigo

obtener_year = lambda parametroDeLaFuncion: f"El año en el que estamos es: {parametroDeLaFuncion}"

print(obtener_year(33))