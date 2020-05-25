import unittest

from HAMM import Mutation


def load_file(filepath):
    with open(filepath) as file:
        seq1 = file.readline()
        seq1 = seq1.strip('\n')
        seq2 = file.readline()
        seq2 = seq2.strip('\n')
    return [seq1, seq2]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_seq = load_file("HAMM_test1.txt")
        mutate = Mutation(input_seq[0], input_seq[1])
        self.assertEqual(mutate.get_result(), 7)

    def test_2(self):
        input_seq = load_file("HAMM_test2.txt")
        mutate = Mutation(input_seq[0], input_seq[1])
        self.assertEqual(mutate.get_result(), 444)


if __name__ == '__main__':
    unittest.main()
