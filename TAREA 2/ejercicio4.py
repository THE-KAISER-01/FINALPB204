def Voc():
    vocales = ['A', 'E', 'I', 'O', 'U']
    letra = input("Ingrese una letra: ").upper()
    
    if letra in vocales:
        print("Es una vocal")
    elif letra not in vocales:
        print("No es una vocal")
    else:
        print("no es una letraa")
    
    

Voc()

