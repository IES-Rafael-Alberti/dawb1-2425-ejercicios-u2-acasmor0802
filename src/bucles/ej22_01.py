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
    final = bucle(palabra)
    final = ', '.join(map(str, final))
    print(final)


if __name__ == "__main__":
    main()