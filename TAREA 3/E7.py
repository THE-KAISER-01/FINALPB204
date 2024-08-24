lista = input("Ingrese una lista de números separados por comas: ")
lista_numeros = [int(numero) for numero in lista.split(",")]

suma = sum(lista_numeros)

print(f"la suma de la lista dada es: {suma}")

