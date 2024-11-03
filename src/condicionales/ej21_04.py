def calcular(num):
    if num%2 == 0:
        return "El número es par."
    else:
        return "El número es impar."


def introduce():
    num = None
    while num == None:
        try:
            num = int(input("Introduce un número: "))
        except ValueError:
            if num is None:
                print("**ERROR** No es un número.")
    return num


def main():
    num = introduce()
    final = calcular(num)
    print(final)



if __name__ == "__main__":
    main()