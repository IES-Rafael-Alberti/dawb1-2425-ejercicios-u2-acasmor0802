def mensaje():
    pass


def calc_din(pts: float) -> float:
    pass


def comprobar_valor(valor: str):
    pass


def recib_punt():
    valor == None

    while valor == None:
        try:
            valor = float(input("Introduzca su puntuación: "))
            comprobar_valor(valor)
        except ValueError:
            if valor is None:
                print("**ERROR** puntaje no valido")


def main():
    pts = recib_punt()
    result = calc_din(pts)
    mensaje(result)



if __name__ == "__main__":
    main()