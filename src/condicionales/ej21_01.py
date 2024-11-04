def comprobar_edad(edad: int):
    if edad < 0:
        raise ValueError("**ERROR** No se puede introducir una edad negativa")
    elif edad > 125:
        raise ValueError("La edad no puede ser superior a 125")



def pedir_edad() -> int:
    edad = None
    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            comprobar_edad(edad)
        except ValueError:
            print("**ERROR** Edad incorrecta")
    
    return edad


def mostrar_anios_cumplidos(edad: int):
    if edad < 18:
        return "No eres mayor de edad"
    else:
        return "Eres mayor de edad"


def main():
    edad = pedir_edad()
    if edad != None:
        print(mostrar_anios_cumplidos(edad))


if __name__ == "__main__":
    main()