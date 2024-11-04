def obtener():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            return numero
        except ValueError as e:
            print(f"La entrada no es correcta: {e}. Intenta de nuevo.")

def main():
    numero = obtener()
    print(f"Has introducido el número: {numero}")

if __name__ == "__main__":
    main()
