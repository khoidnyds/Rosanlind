import unittest

from PROT import Translate


def load_file(filepath):
    with open(filepath) as file:
        input_seq = file.read()
    return input_seq


class MyTestCase(unittest.TestCase):
    def test_1(self):
        protein = Translate(load_file("PROT_test1.txt"))
        self.assertEqual(protein.get_result(), load_file("PROT_test1_expected.txt"))

    def test_2(self):
        protein = Translate(load_file("PROT_test2.txt"))
        self.assertEqual(protein.get_result(), load_file("PROT_test2_expected.txt"))


if __name__ == '__main__':
    unittest.main()
