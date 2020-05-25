import unittest

from SUBS import Motif


def load_file(filepath):
    with open(filepath) as file:
        seq1 = file.readline()
        seq1 = seq1.strip('\n')
        seq2 = file.readline()
        seq2 = seq2.strip('\n')
    return [seq1, seq2]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_seq = load_file("SUBS_test1.txt")
        motif = Motif(input_seq[0], input_seq[1])
        self.assertEqual(motif.get_result(), [2, 4, 10])

    def test_2(self):
        input_seq = load_file("SUBS_test2.txt")
        motif = Motif(input_seq[0], input_seq[1])
        self.assertEqual(motif.get_result(), [16, 43, 98, 105, 154, 161, 168, 175, 182, 205, 220, 227, 266, 273,
                                              280, 312, 347, 376, 429, 470, 477, 484, 491, 540, 561, 598, 605,
                                              632, 673, 680, 690, 786, 804, 832, 911, 926])


if __name__ == '__main__':
    unittest.main()
