def bisiesto(anio):

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio_usuario = int(input("Ingrese un año para verificar si es bisiesto: "))

if bisiesto(anio_usuario):
    print(f'El año {anio_usuario} es bisiesto.')
else:
    print(f'El año {anio_usuario} no es bisiesto.')
