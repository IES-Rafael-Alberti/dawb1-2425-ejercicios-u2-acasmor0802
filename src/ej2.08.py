def calc_piramid(valor):
    cad = []
    num = 1
    if valor % 2 != 0:
        while valor > 0:
            valor -= 2
            cad.insert(0,num)
            print(cad)
            num += 2
    elif valor % 2 == 0:
        valor -= 1
        while valor > 0:
            valor -= 2
            cad.insert(0,num)
            print(cad)
            num += 2



def comprobar_num(valor: str):
    if valor == 0:
        raise ValueError("El número no puede ser igual a cero!")
    if valor < 0:
        raise ValueError("El número no puede ser negaivo!")


def introduce():
    valor = None

    while valor == None:
        try:
            valor = int(input("introduce un número: "))
            comprobar_num(valor)
        except ValueError as e:
            if valor is None:
                print("El número introducido no es válido!, Inténtalo de nuevo!")
            else:
                valor = None
                print(f"{e}, Inténtalo de nuevo")
    return valor



def main():
    valor = introduce()
    calc_piramid(valor)


if __name__ == "__main__":
    main()