import unittest

from RNA import Transcribe


def load_file(filepath):
    with open(filepath) as file:
        input_seq = file.read()
    return input_seq


class MyTestCase(unittest.TestCase):
    def test_seq1(self):
        nuc = Transcribe(load_file("RNA_test1.txt"))
        self.assertEqual(nuc.get_rna(), load_file("RNA_test1_expected.txt"))

    def test_seq2(self):
        nuc = Transcribe(load_file("RNA_test2.txt"))
        self.assertEqual(nuc.get_rna(), load_file("RNA_test2_expected.txt"))

    def test_seq3(self):
        nuc = Transcribe(load_file("RNA_test3.txt"))
        self.assertEqual(nuc.get_rna(), load_file("RNA_test3_expected.txt"))

    def test_seq4(self):
        seq = "GATCX"
        with self.assertRaises(ValueError) as error:
            Transcribe(seq)
        self.assertTrue(error.exception.__str__().startswith("Error:"))

    def test_seq5(self):
        seq = ""
        with self.assertRaises(ValueError) as error:
            Transcribe(seq)
        self.assertTrue(error.exception.__str__().startswith("Error:"))


if __name__ == '__main__':
    unittest.main()
