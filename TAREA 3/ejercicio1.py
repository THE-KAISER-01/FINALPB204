def max_in_list(lista):
    maximo = lista[0]
    
    for numero in lista:
        if numero > maximo:
            maximo = numero   
    return maximo

numeros = input("Ingrese una lista de números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]
mayor_numero = max_in_list(numeros)

print("El número mayor en la lista es:", mayor_numero)