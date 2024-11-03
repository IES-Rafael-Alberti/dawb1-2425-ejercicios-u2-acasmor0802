def dividir(numero1,numero2):
    return numero1/numero2


def pedir_num():
    num1 = None
    num2 = None
    while num1 == None:
        try:
            num1 = int(input("Ingresa el primer número: "))

        except ValueError:
            num1 = None
            print("**ERROR** No es un número.")
    
    while num2 == None:
        try:
            num2 = int(input("Ingresa el segundo número: "))

            if num2 == 0:
                raise ValueError("El divisor no puede ser 0.")
            
        except ValueError as e:
            if num2 is None:
                num2 = None
                print("**ERROR** No es un número.")
            else:
                num2 = None
                print(f"**ERROR** {e}")
            
    return num1, num2
        

def main():
    numero1, numero2 = pedir_num()
    final = dividir(numero1, numero2)
    print(final)


if __name__ == "__main__":
    main()