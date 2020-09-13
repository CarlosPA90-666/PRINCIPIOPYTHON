def main():
    numInicial = int(input("Ingrese un numero para crear la secuencia: "))
    serie = ''+str(numInicial)
    for i in range(numInicial-1):
        serie += str(numInicial)

    print(serie)

if __name__ == '__main__':
    main()