def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad == 0:
        raise ValueError("La edad no puede ser cero!")
    if edad > 125:
        raise ValueError("La edad no puede ser superior a 125")




def pedir_edad() -> int:
    edad = None


    while edad == None:
        try:
            edad = int(input("Introduzca su edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
                print(f"**ERROR** El número introducido no es válido!, Inténtalo de nuevo!")
            else:
                edad = None
                print(f"**ERROR** {e}, Inténtalo de nuevo")


    return edad


def mostrar_anios_cumplidos(edad: int):
    for i in range(1, edad + 1):
            print(i)




def main():
    edad = pedir_edad()
    if edad != None:
         mostrar_anios_cumplidos(edad)




if __name__ == "__main__":
    main()