def ingresar_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto de la compra en euros (0 para finalizar): "))
            return monto
        except ValueError:
            print("**ERROR**: Entrada no válida. Por favor, ingrese un número.")

def procesar_monto(monto, total):
    if monto < 0:
        print("**ERROR**: Monto negativo. Por favor, ingrese un monto válido.")
        return total
    return total + monto

def calcular_total(total):
    if total > 1000:
        total *= 0.9
    return total

def main():
    total = 0.0

    while True:
        monto = ingresar_monto()

        if monto == 0:
            break

        total = procesar_monto(monto, total)

    total_final = calcular_total(total)
    print(f"El total a pagar es: €{total_final:.2f}")

if __name__ == "__main__":
    main()
