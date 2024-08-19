def filtrar_palabras(lista_palabras, longitud):
    return [palabra for palabra in lista_palabras if len(palabra) > longitud]

palabras = ["hola", "manzana", "guayaba", "cafe"]
cantidad = int(input("dame palabras de cuantos caracteres o mas: \n"))
resultado = filtrar_palabras(palabras, cantidad)

print(f'Palabras con más de "{cantidad}" caracteres: {resultado}')
