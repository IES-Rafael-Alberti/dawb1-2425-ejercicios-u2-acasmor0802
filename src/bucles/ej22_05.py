def calcular(invertir, int_anual, tiempo):
    lista = []
    for i in range(1,tiempo + 1, 1):
        invertir *= 1 + int_anual / 100
        lista.append(f"Año {i}: {invertir:.2f}\n")
    return lista


def pedir():
    invertir = float(input("Introduce la cantidad a invertir: "))
    int_anual = float(input("Introduce el interés anual: "))
    tiempo = int(input("Introduce la cantidad de años: "))
    return invertir, int_anual, tiempo


def main():
    invertir, int_anual, tiempo = pedir()
    final = calcular(invertir, int_anual, tiempo)
    final = "".join(map(str, final))
    print(final)



if __name__ == "__main__":
    main()