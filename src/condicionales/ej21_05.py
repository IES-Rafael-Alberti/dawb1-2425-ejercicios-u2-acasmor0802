def introduce2():
    num = None
    while num == None:
        try:
            num = int(input("Introduzca sus ingresos: "))
            if num < 1:
                raise ValueError("No puedes tener salario negativo")
            elif num < 1000:
                return int(1)
            else:
                return int(2)
        except ValueError as e:
            if num is None:
                print("**ERROR** El número no es valido.")
            else:
                num = None
                print(f"**ERROR** {e}")


def introduce():
    num = None
    while num == None:
        try:
            num = int(input("Introduzca su edad: "))
            if num < 1:
                raise ValueError("No puedes tener edad negativa")
            elif num < 16:
                return int(1)
            else:
                return int(2)
        except ValueError as e:
            if num is None:
                print("**ERROR** El número no es valido.")
            else:
                num = None
                print(f"**ERROR** {e}")


def main():
    edad = introduce()
    salario = introduce2()
    if edad == 2 and salario == 2:
        print("Tienes que tributar.")
    else:
        print("No tienes que tributar.")




if __name__ == "__main__":
    main()