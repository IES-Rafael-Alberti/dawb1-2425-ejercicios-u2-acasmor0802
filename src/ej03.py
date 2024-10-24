def comprobar(numeros: list) -> bool:
    try:
        all(isinstance(i, float) for i in numeros)
    except ValueError:
        return False


def calcular():
    pass


def pedir_num() -> list:
    numeros = []
    lista = False
    while lista == False:
        numeros = input("Ingresa dos números separados por un espacio: ").split()
        lista = comprobar(numeros)
        if lista == False:
            print("**ERROR** No son 2 números")
            
    return [float(numeros[0]), float(numeros[1])]
        


def main():
    numero1, numero2 = pedir_num()
    print(numero1)
    print(numero2)


if __name__ == "__main__":
    main()