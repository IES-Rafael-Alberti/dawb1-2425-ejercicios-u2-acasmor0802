def calcula(renta):
    if renta<10000:
        return "Le corresponde un tipo impositivo del 5%."
    elif 10000<=renta<20000:
        return "Le corresponde un tipo impositivo del 15%."
    elif 20000<=renta<35000:
        return "Le corresponde un tipo impositivo del 20%."
    elif 35000<=renta<60000:
        return "Le corresponde un tipo impositivo del 30%."
    else:
        return "Le corresponde un tipo impositivo del 45%."


def introduce():
    renta = None
    while renta == None:
        try:
            renta= float(input("Indique su renta anual: "))
        except ValueError:
            renta = None
            print("**ERROR** No es una renta valida")
    return renta


def main():
    renta = introduce()
    final = calcula(renta)
    print(final)


if __name__ == "__main__":
    main()