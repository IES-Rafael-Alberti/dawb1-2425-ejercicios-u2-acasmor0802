def burbuja(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]


def main():
    numeros = [64, 34, 25, 12, 22, 11, 90]
    burbuja(numeros)
    print("Lista ordenada:", numeros)


if __name__ == "__main__":
    main()