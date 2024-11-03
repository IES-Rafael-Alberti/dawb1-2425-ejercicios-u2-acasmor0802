def pago(seccion):
    if seccion == 1:
        return "gratis"
    elif seccion == 2:
        return "5€"
    else:
        return "10€"


def precio(edad):
    if edad < 4:
        return 1
    elif edad < 19:
        return 2
    else:
        return 3


def introduce():
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduzca su edad: "))
            if edad < 1:
                raise ValueError("La edad debe ser un número positivo.")
        except ValueError as e:
            edad = None
            print(f"**ERROR** {e} No es una edad válida, inténtalo de nuevo.")
    return edad


def main():
    edad = introduce()
    seccion = precio(edad)
    dinero = pago(seccion)
    print(f"El dinero por su entrada es de {dinero}")

    


if __name__ == "__main__":
    main()