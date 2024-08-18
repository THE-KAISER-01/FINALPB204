def max_de_tres(x, y, z):
    if x >= y and x >= z:
        print(f"El número mayor es: {x}")
    elif y >= x and y >= z:
        print(f"El número mayor es: {y}")
    else:
        print(f"El número mayor es: {z}")

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

max_de_tres(x, y, z)
