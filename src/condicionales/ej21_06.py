def introduce():
    sexo= input("Indique su sexo (H/M): ")
    nombre = input("Escriba su nombre: ")
    return sexo, nombre

def main():
    sexo, nombre = introduce()

    if (sexo=="M" and nombre.lower()<"m") or (sexo=="H" and nombre.lower()>"n"):
        print("Le corresponde el grupo A.")
        
    else:
        print("Le corresponde el grupo B.")


if __name__ == "__main__":
    main()