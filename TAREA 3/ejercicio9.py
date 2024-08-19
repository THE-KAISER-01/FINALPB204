def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    
    print(f'"A" aparece {vocales["a"]} veces en "{palabra}"')
    print(f'"E" aparece {vocales["e"]} veces en "{palabra}"')
    print(f'"I" aparece {vocales["i"]} veces en "{palabra}"')
    print(f'"O" aparece {vocales["o"]} veces en "{palabra}"')
    print(f'"U" aparece {vocales["u"]} veces en "{palabra}"')

palabra_usuario = input("Ingrese una palabra: ")

contar_vocales(palabra_usuario)
