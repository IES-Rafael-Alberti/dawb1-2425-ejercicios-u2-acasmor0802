def calcular(edad):
    resultado = []
    for i in range(1,edad + 1, 1):
        resultado.append(i)
    return resultado


def comprobar_edad(edad):
    if edad < 0:
        raise ValueError("no puedes tener edad negativa")
    if edad > 125:
        raise ValueError("no puedes tener una edad mayor a 125")


def pedir_edad():
    edad = None
    while edad == None:
        try:
            edad = int(input("Introduzca su edad: "))
            comprobar_edad(edad)
        except ValueError as e:
            if edad is None:
                print(f"**ERROR** {e}, intentalo de nuevo: ")
            else:
                edad = None
                print("**ERROR** eso no es una edad valida, intentalo de nuevo")
    return edad



def main():
    edad = pedir_edad()
    bucle = calcular(edad)
    bucle = ', '.join(map(str, bucle))
    print(bucle)


if __name__ == "__main__":
    main()