edades = (19,12,32,25,32,38,26,14,28,33)
contador = 0

for edad in edades:
    if edad > 20:
        contador += 1
        
print(f"La cantidad de personas con edades superiores a 20 es: {contador}")


# parte dos del codigo donde pide las edades:
edades_usuario = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    edades_usuario.append(edad)

contador_usuario = 0

for edad in edades_usuario:
    if edad > 20:
        contador_usuario += 1

print(f"La cantidad de personas con edades superiores a 20 es: {contador_usuario}" )