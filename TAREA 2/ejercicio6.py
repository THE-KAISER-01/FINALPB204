def inversa(cadena):
    Cadena_invertida = ""
    for char in cadena:
        Cadena_invertida=char+Cadena_invertida
    return Cadena_invertida
        
print(inversa("hola mundo"))

