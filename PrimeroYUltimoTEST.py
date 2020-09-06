import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        Palabra = 'Quesadilla'
        PrimerCaracter = Palabra[0]
        SegundoCaracter = Palabra[len(Palabra)-1]

        self.assertEqual('Q', PrimerCaracter)
        self.assertEqual('a', SegundoCaracter)


if __name__ == '__main__':
    unittest.main()
