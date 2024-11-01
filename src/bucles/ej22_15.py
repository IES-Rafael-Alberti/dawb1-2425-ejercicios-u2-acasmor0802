def suma(num, total):
    total += num
    return total


def introducir():
    num = None
    while num == None:
        try:
            num = int(input("Introduce un número entero: "))
        except ValueError:
            num == None
            print("**ERROR** eso no es un número entero")
    return num


def main():
    total = 0
    while True:
        num = introducir()
        if num == 0:
            print(total)
            break
        else:
             total = suma(num, total)


if __name__ == "__main__":
    main()