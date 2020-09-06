def PrimeroYUltimo(Palabra):

    Caracter1 = Palabra[0]
    CaracterFinal = Palabra[len(Palabra) - 1]
    return(Caracter1,CaracterFinal)

def main():

    Palabra = input("Introduzca una palabra: ")

    (caracterUno,CaracterFinal) = PrimeroYUltimo(Palabra)

    print("Primer caracter: ",caracterUno)

    print("Ultimo caracter: ",CaracterFinal)

if __name__ == '__main__':
    main()