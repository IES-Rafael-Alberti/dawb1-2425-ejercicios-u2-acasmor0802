def comprobar(num):
    if num == 2:
        cuenta = 1
        return cuenta
    else:
        for i in range(2,num,1):
            if num%i == 0:
                cuenta = 0
                return cuenta
            else:
                cuenta = 1
        return cuenta


def comprobacion(num):
    if num == 1 or num<0:
        raise ValueError("No es un número mayor a 1, intentalo de nuevo")


def ingresar():
    num = None
    while num == None:
        try:
            num = int(input("Introduce un número mayor a 1: "))
            comprobacion(num)
        except ValueError as e:
            if num is None:
                print("No es un número mayor a 1, intentalo de nuevo")
            else:
                num = None
                print(f"{e}")
    return num


def main():
    programa = True
    lista = 0
    while programa:
        num = ingresar()
        if num == 0:
            programa = False
        else:
            cuenta = comprobar(num)
            lista += cuenta
    print(f"Se ingresaron {lista} números primos.")


if __name__ == "__main__":
    main()