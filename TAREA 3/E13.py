entrada_nombres = input("Ingresa una lista de nombres separados por comas: ")

nombres = [nombre.strip() for nombre in entrada_nombres.split(",")]

nombres.sort()

print("Lista de nombres ordenada alfabéticamente:")
for nombre in nombres:
    print(nombre)
