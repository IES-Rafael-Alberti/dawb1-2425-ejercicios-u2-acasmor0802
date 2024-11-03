def obtener():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                raise ValueError("El número debe ser positivo.")
            return numero
        except ValueError as e:
            print(f"**ERROR** {e}. Intenta de nuevo.")

def cuenta_atras(numero):
    cuenta = []
    for n in range(numero, -1, -1):
        cuenta.append(str(n))
    return cuenta

def mostrar_cuenta_atras(cuenta):
    resultado = ", ".join(cuenta)
    return resultado

def main():
    numero = obtener()
    cuenta = cuenta_atras(numero)
    print(mostrar_cuenta_atras(cuenta))

if __name__ == "__main__":
    main()
