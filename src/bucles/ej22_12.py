def comprobacion(letra,frase):
    return frase.count(letra)



def introduce_letra():
    letra = None
    while letra == None:
        letra = input("introduce una letra: ")
        if len(letra) != 1:
            letra = None
            print("**ERROR** no se puede introducir una letra")
    return letra


def introduce_frase():
    frase = input("Introduce una frase: ")
    return frase


def main():
    frase = introduce_frase()
    letra = introduce_letra()
    repeticiones = comprobacion(letra,frase)
    print(f"La letra {letra} aparece {repeticiones} en la frase.")


if __name__ == "__main__":
    main()