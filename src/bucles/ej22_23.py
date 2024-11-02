def mostrar(frase):
    frase = ", ".join(map(str, frase))
    digitos = [caracter for caracter in frase if caracter.isdigit()]
    cantidad = len(digitos)
    return cantidad


def introduce():
    frase = input("Libro: ")
    return frase


def main():
    frase = []
    programa = True
    while programa:
        almacen = introduce()
        frase.append(almacen)
        if almacen == "*":
            frases = int(len(frase))
            frases-= 1
            programa = False
        elif almacen == "/":
            print(f"Línea completa. Aparecen {mostrar(frase)} dígitos numéricos.")
            frase = []
    print(f"Fin. Se leyeron {frases} lineas completas.")



if __name__ == "__main__":
    main()