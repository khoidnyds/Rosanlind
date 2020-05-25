import re


class Complement:
    """ Problem Complementing a Strand of DNA
    In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
    The reverse complement of a DNA string s
    is the string sc formed by reversing the symbols of s
    , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s

    Sample Dataset
    AAAACCCGGT
    Sample Output
    ACCGGGTTTT
    """

    def __init__(self, seq):
        if seq == "":
            raise ValueError("Error: Empty input.")
        if not re.compile("^[ACGT]+$").match(seq):
            raise ValueError("Error: Input contains invalid character.")

        self.__seq = seq
        self.__complement()

    def __complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        self.__seq = "".join(complement_dict[letter] for letter in self.__seq)
        self.__seq = self.__seq[::-1]

    def get_complement(self):
        return self.__seq
