def sum(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado

def multip(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

# Ejemplo de uso
numeros = [1, 2, 3, 4]

print("La suma de los números es:", sum(numeros))
print("La multiplicación de los números es:", multip(numeros))
