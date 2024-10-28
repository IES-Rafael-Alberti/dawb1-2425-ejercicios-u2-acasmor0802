def calcular(num) -> bool:
    if num == 1:
        return False
    for i in range(2, num):
        if num %i == 0:
            return False
    return True


def comprobar_num(num):
    if num < 0:
        raise ValueError("El número ebe ser positivo")
    if num == float:
        raise ValueError("El número debe ser un número entero")


def pedir_num():
    num = None
    while num == None:
        try:
            num = int(input("Introduzca un número entero positivo: "))
            comprobar_num(num)
        except ValueError as e:
            if num is None:
                print("**ERROR** eso no es un número valido, intentalo de nuevo: ")
            else:
                num = None
                print(f"**ERROR** {e} , intentalo de nuevo")
    return num


def main():
    num = pedir_num()
    final = calcular(num)
    if final == True:
        print(f"{num} es un número primo")
    else:
        print(f"{num} no es un número primo")


if __name__ == "__main__":
    main()