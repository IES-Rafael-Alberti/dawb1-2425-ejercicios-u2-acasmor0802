def bucle(palabra):
    a = 10
    resultado = []
    while a != 0:
        a -= 1
        resultado.append(palabra)
    return resultado


def pedir_palabra():
    palabra = input("Introduce una palabra: ")
    return palabra


def main():
    palabra = pedir_palabra()
    hola = bucle(palabra)
    hola = ', '.join(map(str, hola))
    print(hola)


if __name__ == "__main__":
    main()