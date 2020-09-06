import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        EdadActualidad = 15
        AnioActualidad= 2020
        EdadEstimada=EdadActualidad +(2070-AnioActualidad)

        self.assertEqual(EdadEstimada, 65)


if __name__ == '__main__':
    unittest.main()
