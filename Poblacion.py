def main():

    PrimeraPoblacion = 35
    SegundaPoblacion = 19.9
    PorcentajePrimeraPoblacion = 0.02
    PorcentajeSegundaPoblacion = 0.03

    while PrimeraPoblacion > SegundaPoblacion:
        PrimeraPoblacion = PrimeraPoblacion + (PrimeraPoblacion * PorcentajePrimeraPoblacion)
        SegundaPoblacion = SegundaPoblacion + (SegundaPoblacion * PorcentajeSegundaPoblacion)


    print("Supera la primera Poblacion cuando son ",SegundaPoblacion," Millones")

if __name__ == "__main__":
    main()