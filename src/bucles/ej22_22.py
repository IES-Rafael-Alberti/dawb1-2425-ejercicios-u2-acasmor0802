def calcular(num):
    pares = 0
    impares = 0

    for i in str(num):
        if int(i) % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


def ingresar():
    while True:
        try:
            num = int(input("Ingresa un número entero positivo (0 para salir): "))
            if num >= 0:
                return num
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Inténtalo de nuevo.")


def main():
    total_pares = 0
    total_impares = 0
    programa = True

    while programa:
        num = ingresar()
        if num == 0:
            programa = False
        else:
            pares, impares = calcular(num)
            print(f"El número tiene {pares} dígitos pares y {impares} dígitos impares.")
            total_pares += pares
            total_impares += impares

    print(f"En total hay {total_pares} dígitos pares y {total_impares} dígitos impares.")


if __name__ == "__main__":
    main()
