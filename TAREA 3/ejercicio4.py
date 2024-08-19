def contar_mayus(cadena):
    mayusculas = sum(1 for caracter in cadena if caracter.isupper())
    return mayusculas

cadena_usuario = input("Ingresa una cadena: ")

numero_mayusculas = contar_mayus(cadena_usuario)
print(f"La cadena tiene {numero_mayusculas} letras mayúsculas.")
