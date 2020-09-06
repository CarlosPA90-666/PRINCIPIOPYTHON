import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        PrimeraPoblacion = 35
        SegundaPoblacion = 19.9
        PorcentajePrimeraPoblacion = 0.02
        PorcentajeSegundaPoblacion = 0.03

        while PrimeraPoblacion > SegundaPoblacion:

            PrimeraPoblacion = PrimeraPoblacion + (PrimeraPoblacion * PorcentajePrimeraPoblacion)

            SegundaPoblacion = SegundaPoblacion + (SegundaPoblacion * PorcentajeSegundaPoblacion)

        self.assertTrue(SegundaPoblacion>PrimeraPoblacion)



if __name__ == '__main__':
    unittest.main()
