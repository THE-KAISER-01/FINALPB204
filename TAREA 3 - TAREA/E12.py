import random
numero_aleatorio = random.randint(1, 100)

intentos = 0
adivinado = False
print("------------BIENVENIDO------------\n")
print("He elegido un número entre 1 y 100. Intenta adivinarlo.")

while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento < numero_aleatorio:
        print("El número es mayor. Intenta nuevamente.")
    elif intento > numero_aleatorio:
        print("El número es menor. Intenta nuevamente.")
    else:
        adivinado = True
        print(f"\n¡Felicidades! Has adivinado el número en {intentos} intentos.")
