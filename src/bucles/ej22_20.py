def introducir_letra():
    letra = None
    while letra == None:
        letra = input("Introduce una letra: ")
        if len(letra) != 1:
            letra = None
            print("**ERROR** solo una letra")
    return letra


def introducir_frase():
    frase = input("Introduce una frase: ")
    return frase


def encontrar_letra(frase, letra):
    posiciones = []
    for posicion, caracter in enumerate(frase):
        if caracter == letra:
            posiciones.append(posicion)
    
    return posiciones


def main():
    frase = introducir_frase()
    letra = introducir_letra()
    posiciones = encontrar_letra(frase, letra)

    if posiciones:
        for posicion in posiciones:
            print(f"Se encontró la letra '{letra}' en la posición {posicion}.")
    else:
        print(f"No se encontró la letra '{letra}' en la frase.")


if __name__ == "__main__":
    main()