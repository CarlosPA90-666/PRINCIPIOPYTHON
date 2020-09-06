def edad2070(edad, anio):
    Edad2070 = 2070 - anio
    return (Edad2070 + edad)


def main():
    edad = int(input("Introduzca su edad Actual: "))

    anio = int(input("Introduzca el anio actual: "))

    print("Su edad en el 2070 sera " ,(edad2070(edad, anio)))


if __name__ == '__main__':
    main()
