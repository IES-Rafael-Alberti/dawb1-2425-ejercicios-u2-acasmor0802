def mayor(lista):
    return max(lista)


def comprobacion(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo")
    elif num >= 10:
        raise ValueError("El número no puede ser igual o mayor a 10")
    elif num == float:
        raise ValueError("El número debe ser entero")


def introduce():
    num = None
    while not num:
        try:
            num = int(input("Introduce un número entero positivo menor a 10: "))
            if num == 0:
                return num
            comprobacion(num)
        except ValueError as e:
            if num is None:
                print("**ERROR** número no introducido")
            else:
                num = None
                print(f"**ERROR** {e}, intentalo de nuevo")
    return num


def main():
    lista = []
    while True:
        num = introduce()
        lista.append(num)
        if num == 0:
            break
    print(mayor(lista))


if __name__ == "__main__":
    main()