def reverir(palabra):
    for letra in reversed(palabra):
        print(letra)


def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    reverir(palabra)


def main():
    pedir_palabra()


if __name__ == "__main__":
    main()