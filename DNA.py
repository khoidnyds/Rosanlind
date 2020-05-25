import re
from collections import Counter


class Count:
    """ Problem: Counting DNA Nucleotides
    A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length
    of a string is the number of symbols that it contains.
    An example of a length 21 DNA string
    (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

    Given: A DNA string s
    of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that
    the symbols 'A', 'C', 'G', and 'T' occur in s

    Sample Dataset
    AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
    Sample Output
    20 12 17 21
    """

    def __init__(self, seq):
        if seq == "":
            raise ValueError("Error: Empty input.")
        if not re.compile("^[ACGT]+$").match(seq):
            raise ValueError("Error: Input contains invalid character.")

        self.__seq = seq
        self.__res = dict()
        self.__count()

    def __count(self):
        self.__res = Counter(self.__seq)

    def get_nuc(self):
        return [self.__res.get('A'),
                self.__res.get('C'),
                self.__res.get('G'),
                self.__res.get('T')]
