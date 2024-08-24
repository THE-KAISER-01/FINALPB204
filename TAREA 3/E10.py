entrada_calificaciones = input("Ingresa las calificaciones separadas por comas: ")

calificaciones = [float(calificacion) for calificacion in entrada_calificaciones.split(",")]

promedio = sum(calificaciones) / len(calificaciones)

print(f"El promedio de las calificaciones es: {promedio:.2f}")
