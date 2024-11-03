def ingrediente(eleccion,vegetal,no_vegetal):
    final = None
    vegetal = ", ".join(map(str, vegetal))
    no_vegetal = ", ".join(map(str, no_vegetal))
    while final == None:
        if eleccion == 1:
            final = input(f"¿Cuál ingrediente desea ponerle a la pizza además de mozzarela y tomate?\nOpciones: {vegetal}\n -")
            if final in vegetal:
                return final
            else:
                final = None
                print("Intentalo de nuevo")
        else:
            final = input(f"¿Cuál ingrediente desea ponerle a la pizza además de mozzarela y tomate?\n Opciones: {no_vegetal}\n -")
            if final in no_vegetal:
                return final
            else:
                final = None
                print("Intentalo de nuevo")


def menu():
    menu = None
    while menu == None:
        menu = input("¿Desea una pizza vegetariana?: ")
        verificaccion = menu.lower()
        if verificaccion == "si":
            return int(1)
        elif verificaccion == "no":
            return int(2)
        else:
            menu = None
            print("Respuestas validas: si y no, intentalo de nuevo")


def main():
    vegetal = ["pimiento", "tofu"]
    no_vegetal = ["peperoni", "jamon", "salmon"]
    eleccion = menu()
    parte = ingrediente(eleccion, vegetal, no_vegetal)
    print(f"La pizza lleva los ingredientes tomate, mozzarela y {parte}")


if __name__ == "__main__":
    main()