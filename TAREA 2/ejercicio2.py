def max_de_tres():
  
    if x>=y:
        if x>=z:
            return x
        else:
            return z
    else:
        if y>=z:
            return y
        else:
            return z
    

x=int(input("ingrese el primer numero: "))
y=int(input("ingrese el segundo numero: "))
z=int(input("ingrese el  tercer numero: "))

print("El numero mayor de los tres es: ",max_de_tres())


            