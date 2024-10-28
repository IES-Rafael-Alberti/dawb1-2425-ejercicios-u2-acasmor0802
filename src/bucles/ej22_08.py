def calcular(num):
    resultado = ""
    for i in range(0,num+1, 2):
        for j in range(i+1, 0, -2):
            resultado += str(j) + " "
        resultado += "\n"
    return resultado

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
    print(final)


if __name__ == "__main__":
    main()