def contraseña():
    contraseña_correcta = input("Establece la contraseña: ")
    while True:
        try:
            contraseña = input("Introduce la contraseña: ")

            if contraseña != contraseña_correcta:
                raise ValueError("Incorrect Password!!")
            
            return "Contraseña correcta."
        except ValueError as e:
            contraseña = None
            print(f"{e}")


def main():
    contrasena = contraseña()
    print(contrasena)


if __name__ == "__main__":
    main()
