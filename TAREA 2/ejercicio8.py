def superposicion(lista1, lista2):

    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True  
    return False 

lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6, 7]

resultado = superposicion(lista1, lista2)

print("¿Las listas tienen al menos un miembro en común?",resultado)
