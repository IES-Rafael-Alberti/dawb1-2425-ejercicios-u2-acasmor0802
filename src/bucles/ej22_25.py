def mas_largo(palabras):
    largo = max(palabras, key=len)
    return largo


def introducir():
    frase = input("Introduce una frase: ")
    return frase


def main():
    frase = introducir()
    palabras = frase.split()
    largo = mas_largo(palabras) 
    print(f"La frase tiene {palabras} palabras y la palabra más larga es {largo}")


if __name__ == "__main__":
    main()