año_en_curso = int(input("ingrese el año en curso:\n "))
lista = []
for i in range(3):
    i += 1
    nombre = input(f"Ingrese el nombre {i}:\n ")
    nac = int(input(f"año de nacimiento {i}:\n "))
    
    edad = año_en_curso-nac +1
    lista.append((nombre,edad))

print("\nEdades al final del curso: ")
print()
for nombre, edad in lista:
    print(f'"{nombre}" al final del curso tendra: {edad}')


