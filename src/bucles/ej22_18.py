def suma(num):
    suma = 0
    for i in range(0,num+1,1):
        suma += i
    return suma


def resultado(lista):
    resultado = []
    for i in lista:
        if i%2==0:
            resultado.append(i)

    resultado = ", ".join(map(str,resultado[:-1])) + " y " + str(resultado[-1])
    return resultado



def comprobacion(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo")


def introduce():
    num = None
    while not num:
        try:
            num = int(input("Introduce un número entero positivo: "))
            if num == -1:
                return num
            comprobacion(num)
        except ValueError as e:
            if num is None:
                print("**ERROR** es necesario introducir un número, intentalo de nuevo")
            else:
                num = None
                print(f"**ERROR** {e}, intentalo de nuevo")
    return num


def main():
    lista = []
    final = False
    while not final:
        num = introduce()
        if num == -1:
            final = True
        else:
            lista.append(num)
            print(suma(num))
    print(f"Los números {resultado(lista)} son pares")


if __name__ == "__main__":
    main()