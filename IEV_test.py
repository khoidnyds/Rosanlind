import unittest

from IEV import Offspring


class MyTestCase(unittest.TestCase):
    def test_1(self):
        offspring = Offspring(1, 0, 0, 1, 0, 1)
        self.assertAlmostEqual(offspring.get_result(), 3.5, 5)

    def test_2(self):
        offspring = Offspring(18882, 17577, 16737, 18765, 16122, 18677)
        self.assertAlmostEqual(offspring.get_result(), 150661.5, 5)


if __name__ == '__main__':
    unittest.main()
