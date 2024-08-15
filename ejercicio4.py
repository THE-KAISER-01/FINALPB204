def Voc():
    vocales = ['A', 'E', 'I', 'O', 'U']
    letra = input("Ingrese una letra: ").upper()
    
    if letra in vocales:
        print("Es una vocal")
    else:
        print("No es una vocal")
    

Voc()

