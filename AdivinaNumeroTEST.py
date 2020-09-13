import unittest
import random


class MyTestCase(unittest.TestCase):
    def test_something(self):
        numeroadivinar= random.randint(1,1000)
        numeroingresado=int(input("Ingrese un numero entre 1 y 1000:  "))

        while numeroadivinar != numeroingresado:
            if numeroingresado<numeroadivinar:
                print('el numero secreto es mayor a ',numeroingresado)
            if numeroingresado>numeroadivinar:
                print('el numero secreto es menor a ',numeroingresado)
            if numeroingresado==numeroadivinar:
                break
            else:
                numeroingresado=int(input("Ingrese un numero entre 1 y 1000:  "))

        if numeroingresado==numeroadivinar:
            print('felicitaciones encontro el numero secreto ---> ', numeroadivinar)


        self.assertEqual(numeroingresado, numeroadivinar)


if __name__ == '__main__':
    unittest.main()
