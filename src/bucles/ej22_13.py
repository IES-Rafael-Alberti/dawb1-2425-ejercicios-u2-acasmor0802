def eco(frase):
    print(frase)

def introduce_frase():
    frase = input("Introduce una frase (escribe 'salir' para terminar): ")
    return frase

def main():
    while True:
        frase = introduce_frase()
        if frase.lower() == "salir":
            print("Programa terminado.")
            break
        eco(frase)

if __name__ == "__main__":
    main()
