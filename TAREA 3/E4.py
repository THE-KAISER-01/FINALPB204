from datetime import date

anio = int(input("Ingresa tu año de nacimiento: "))
mes = int(input("Ingresa tu mes de nacimiento: "))
dia = int(input("Ingresa tu día de nacimiento: "))

fecha_nacimiento = date(anio, mes, dia)
fecha_actual = date.today()

dias_transcurridos = (fecha_actual - fecha_nacimiento).days

print(f"Han pasado {dias_transcurridos} días desde tu nacimiento.")
