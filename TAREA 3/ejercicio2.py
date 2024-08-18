def mas_larga(lista_palabras):
    if not lista_palabras:
        return None 
    
    palabra_larga = lista_palabras[0]  
    
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra 
    
    return palabra_larga
