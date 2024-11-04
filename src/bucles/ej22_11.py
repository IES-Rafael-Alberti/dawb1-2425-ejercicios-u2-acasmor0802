def reverir(palabra):
    lista = []
    for letra in reversed(palabra):
        lista.append(letra)
    lista = "".join(map(str, lista))
    return lista


def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    return reverir(palabra)


def main():
    print(pedir_palabra())


if __name__ == "__main__":
    main()