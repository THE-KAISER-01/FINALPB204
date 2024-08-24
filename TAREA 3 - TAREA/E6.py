archivo_nombre = input("Ingresa el nombre del archivo de texto (incluyendo la extensión, por ejemplo, 'archivo.txt'): ")

with open(archivo_nombre, 'r') as archivo:
        contenido = archivo.read()
        print("\nContenido del archivo:\n")
        print(contenido)

