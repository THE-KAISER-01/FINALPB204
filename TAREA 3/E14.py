numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print("")
