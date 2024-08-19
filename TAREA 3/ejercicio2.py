list_palabras = ["hola", "manzana", "guayaba", "cafe"]
longitud = 0
palabra_larga = 0


for palabras in list_palabras:
    if len(palabras) > longitud:
        longitud = len(palabras)
        palabra_larga = palabras

print(palabra_larga)