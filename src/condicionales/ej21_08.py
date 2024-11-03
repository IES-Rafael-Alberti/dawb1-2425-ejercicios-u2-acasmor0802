def calc_din(pts: float) -> str:
    if pts == 0.0:
        return "Inaceptable, obtienes 0€"
    elif pts == 0.4:
        dinero = 2400 * pts
        return f"Aceptable, obtienes {dinero}€"
    elif pts >= 0.6:
        dinero = 2400 * pts
        return f"Meritorio, obtienes {dinero}€"
    else:
        raise ValueError("**ERROR** valor desconocido")
    

def comprobar_valor(valor: float):
    if valor != 0.0 and valor != 0.4 and valor < 0.6:
        raise ValueError("**ERROR** valor desconocido")
    

def recib_punt() -> float:
    valor = None

    while valor is None:
        try:
            valor = float(input("Introduzca su puntuación (0.0, 0.4, 0.6 o más): "))
            comprobar_valor(valor)
        except ValueError as e:
            valor = None
            print(f"**ERROR** {e}, intentalo de nuevo.")

    return valor


def main():
    pts = recib_punt()
    result = calc_din(pts)
    print(result)


if __name__ == "__main__":
    main()
