import unittest

from DNA import Count


def load_file(filepath):
    with open(filepath) as file:
        input_seq = file.read()
    return input_seq


class MyTestCase(unittest.TestCase):

    def test_seq1(self):
        seq = load_file("DNA_test1.txt")
        nuc_count = Count(seq)
        self.assertEqual(nuc_count.get_nuc(), [20, 12, 17, 21])

    def test_seq2(self):
        seq = load_file("DNA_test2.txt")
        nuc_count = Count(seq)
        self.assertEqual(nuc_count.get_nuc(), [246, 260, 254, 239])

    def test_seq3(self):
        seq = load_file("DNA_test3.txt")
        nuc_count = Count(seq)
        self.assertEqual(nuc_count.get_nuc(), [233, 238, 260, 244])

    def test_seq4(self):
        seq = "GATCX"
        with self.assertRaises(ValueError) as error:
            Count(seq)
        self.assertTrue(error.exception.__str__().startswith("Error:"))

    def test_seq5(self):
        seq = ""
        with self.assertRaises(ValueError) as error:
            Count(seq)
        self.assertTrue(error.exception.__str__().startswith("Error:"))


if __name__ == '__main__':
    unittest.main()
