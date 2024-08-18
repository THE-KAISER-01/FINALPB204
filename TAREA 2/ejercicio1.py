def MAX(x, y):
    if x >= y:
        mayor = x
    else:
        mayor = y
    
    print(f"El número mayor es: {mayor}")

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

MAX(x, y)
