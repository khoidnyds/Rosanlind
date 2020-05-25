import unittest

from IPRB import Mendel


class MyTestCase(unittest.TestCase):
    def test_1(self):
        mendel = Mendel(2, 2, 2)
        self.assertAlmostEqual(mendel.get_result(), 0.78333, 5)

    def test_2(self):
        mendel = Mendel(15, 16, 17)
        self.assertAlmostEqual(mendel.get_result(), 0.732269503, 5)

    def test_3(self):
        mendel = Mendel(86, 21, 25)
        self.assertAlmostEqual(mendel.get_result(), 0.928868841, 5)


if __name__ == '__main__':
    unittest.main()
