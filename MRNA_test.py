import unittest

from MRNA import MRNA


def load_file(filepath):
    with open(filepath) as file:
        input_seq = file.read()
    return input_seq


class MyTestCase(unittest.TestCase):
    def test_1(self):
        mrna = MRNA("MA", 1000000)
        self.assertEqual(mrna.get_result(), 12)

    def test_2(self):
        mrna = MRNA(load_file("MRNA_test1.txt"), 1000000)
        self.assertEqual(mrna.get_result(), 561024)


if __name__ == '__main__':
    unittest.main()
