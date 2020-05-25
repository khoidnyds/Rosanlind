import unittest

from LIA import Mendel2


class MyTestCase(unittest.TestCase):
    def test_seq1(self):
        nuc = Mendel2(2, 1)
        self.assertAlmostEqual(nuc.get_result(), 0.684, 3)

    def test_seq2(self):
        nuc = Mendel2(7, 31)
        self.assertAlmostEqual(nuc.get_result(), 0.6142569731, 7)


if __name__ == '__main__':
    unittest.main()
