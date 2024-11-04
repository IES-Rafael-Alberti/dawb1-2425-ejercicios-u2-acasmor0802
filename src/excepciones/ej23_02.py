def obtener():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                raise ValueError("El número debe ser positivo.")
            return numero
        except ValueError as e:
            print(f"**ERROR** {e}. Intenta de nuevo.")


def generar_imp(numero):
    impares = []
    for n in range(1, numero + 1):
        if n % 2 != 0:
            impares.append(str(n))
    return impares


def mostrar_imp(impares):
    resultado = ", ".join(impares)
    return resultado


def main():
    numero = obtener()
    impares = generar_imp(numero)
    print(mostrar_imp(impares))


if __name__ == "__main__":
    main()