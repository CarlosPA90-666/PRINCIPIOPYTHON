import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        numInicial= 10
        serie = ''+str(numInicial)
        for i in range(numInicial-1):
            serie += str(numInicial)

        self.assertEqual(serie, '10101010101010101010')


if __name__ == '__main__':
    unittest.main()
