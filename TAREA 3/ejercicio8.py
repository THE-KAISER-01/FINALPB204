lista = ["jesus", "abdias", "alejandro", "kevin", "leonel"]

contador = 0
for nombre in lista:
    if nombre.lower().startswith('a'):
        contador +=1

print(f'la cantidad de nombres que contiene "a" son: \n {contador}')

# ELEGIR QUÉ LETRA BUSCAR
letra_usuario = input("¿Qué letra desea buscar?: \n").upper()

contador = 0
for nomb in lista:
    if nomb.upper().startswith(letra_usuario):
        contador += 1

print(f'La cantidad de nombres que comienzan con "{letra_usuario}" son: \n{contador}')