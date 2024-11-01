import os


def limpiar():
    try:
        comando = "cls" if os.name == "nt" else "clear" 
        os.system(comando)
    except Exception as e:
        print(f"Problemas al intentar limpiar programa")


def accion(opcion, programa):
    if opcion == 1:
        return print("texto")
    elif opcion == 2:
        return print("texto2")


def comprobar(opcion: int) -> bool:
    return 1 <= opcion <= 3


def mostrar_menu():
    print("1- Comenzar programa")
    print("2- Imprimir listado")
    print("3- Finalizar programa")


def main():
    programa = False
    limpiar()
    while programa == False:
        mostrar_menu()
        opcion = int(input(""))
        if comprobar(opcion):
            limpiar()
            if opcion == 3:
                programa = True
            else:
                accion(opcion,programa)
            
        else:
            limpiar()
            print("**ERROR** opción no valida")
    limpiar()


if __name__ == "__main__":
    main()