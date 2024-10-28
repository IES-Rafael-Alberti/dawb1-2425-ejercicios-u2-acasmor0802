def tabla1():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"1 * {i} = {i}"
        resultado += "\n"
    return resultado


def tabla2():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"2 * {i} = {i*2}"
        resultado += "\n"
    return resultado


def tabla3():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"3 * {i} = {i*3}"
        resultado += "\n"
    return resultado


def tabla4():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"4 * {i} = {i*4}"
        resultado += "\n"
    return resultado


def tabla5():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"5 * {i} = {i*5}"
        resultado += "\n"
    return resultado


def tabla6():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"6 * {i} = {i*6}"
        resultado += "\n"
    return resultado


def tabla7():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"7 * {i} = {i*7}"
        resultado += "\n"
    return resultado


def tabla8():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"8 * {i} = {i*8}"
        resultado += "\n"
    return resultado


def tabla9():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"9 * {i} = {i*9}"
        resultado += "\n"
    return resultado


def tabla10():
    resultado = ""
    for i in range(0, 11, 1):
        resultado += f"10 * {i} = {i*10}"
        resultado += "\n"
    return resultado


def main():
    print(tabla1() + "\n" + tabla2() + "\n" + tabla3() + "\n" + tabla4() + "\n" + tabla5() + "\n" + tabla6() + "\n" + tabla7() + "\n" + tabla8() + "\n" + tabla9() + "\n" + tabla10())


if __name__ == "__main__":
    main()