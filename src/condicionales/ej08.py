def mensaje():
    pass


def calc_din(pts: float) -> float:
    if pts == 0.0:
        return "Inaceptable, obtienes 0€"
    if pts == 0.4:
        return ""
    if pts == 0.6:
        raise ValueError("**ERROR** valor desconocido")


def comprobar_valor(valor: str):
    if valor == 0.1:
        raise ValueError("**ERROR** valor desconocido")
    if valor == 0.2:
        raise ValueError("**ERROR** valor desconocido")
    if valor == 0.3:
        raise ValueError("**ERROR** valor desconocido")
    if valor == 0.5:
        raise ValueError("**ERROR** valor desconocido")


def recib_punt():
    valor == None

    while valor == None:
        try:
            valor = float(input("Introduzca su puntuación: "))
            comprobar_valor(valor)
        except ValueError as e:
            if valor is None:
                print("**ERROR** puntaje no valido, intentalo de nuevo")
            else:
                valor = None
                print(f"**ERROR** {e},intentalo de nuevo")


def main():
    pts = recib_punt()
    result = calc_din(pts)
    mensaje(result)



if __name__ == "__main__":
    main()