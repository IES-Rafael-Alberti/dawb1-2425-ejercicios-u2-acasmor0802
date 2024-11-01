def calcula(num):
    suma = 0
    for i in range(0,num+1,1):
        suma += i
    return suma


def comprobacion(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo")
    elif num == float:
        raise ValueError("El número debe ser entero")


def introduce():
    num = None
    while not num:
        try:
            num = int(input("Introduce un número entero positivo: "))
            comprobacion(num)
        except ValueError as e:
            if num is None:
                print("**ERROR** número no introducido")
            else:
                num = None
                print(f"**ERROR** {e}, intentalo de nuevo")
    return num


def main():
    num = introduce()
    suma = calcula(num)
    print(suma)


if __name__ == "__main__":
    main()