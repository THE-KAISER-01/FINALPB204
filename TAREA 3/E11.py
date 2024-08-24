print("------- BIENVENIDO CALCULA TU IMC---------\n")

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
