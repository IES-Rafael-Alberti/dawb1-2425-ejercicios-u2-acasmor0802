def obtener_edad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 1:
                raise ValueError("La edad debe ser un número positivo.")
            return edad
        except ValueError as e:
            print(f"**ERROR** {e}. Intenta de nuevo.")

def generar_anios(edad):
    return [str(año) for año in range(1, edad + 1)]

def mostrar_anios(anios):
    resultado = ", ".join(anios)
    return resultado

def main():
    edad = obtener_edad()
    anios = generar_anios(edad)
    print(mostrar_anios(anios))

if __name__ == "__main__":
    main()
