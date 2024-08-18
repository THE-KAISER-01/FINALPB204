def calcular_longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador

mi_lista = input("Dame los números separados por espacios: ").replace(" ", "")
mi_cadena = input("Dame la cadena: ").replace(" ", "")

longitud_lista = calcular_longitud(mi_lista)
longitud_cadena = calcular_longitud(mi_cadena)

print("La longitud de la lista es: ",longitud_lista)
print("La longitud de la cadena es: ",longitud_cadena)
