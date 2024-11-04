def comprobar_contraseña(intento: str, contraseña: str) -> bool:
    if contraseña == intento:
        return True
    else:
        return False


def crear_contraseña() -> str:
    contraseña = []
    contraseña = input("Escribe una contraseña: ")
    return contraseña


def main():
    contraseña = crear_contraseña()
    comprobacion = False
    while comprobacion != True:
        intento = input("Introduce la contraseña: ")
        verificacion = comprobar_contraseña(intento, contraseña)
        if verificacion == True:
            print("Contraseña corecta")
            comprobacion = True
        else:
            print("contraseña equivocada")
            comprobacion = False


if __name__ == "__main__":
    main()