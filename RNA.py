import re


class Transcribe:
    """ Problem Transcribing DNA into RNA
    An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
    Given a DNA string t corresponding to a coding strand,
    its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u

    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t

    Sample Dataset
    GATGGAACTTGACTACGTAAATT
    Sample Output
    GAUGGAACUUGACUACGUAAAUU
    """

    def __init__(self, seq):
        if seq == "":
            raise ValueError("Error: Empty input.")
        if not re.compile("^[ACGT]+$").match(seq):
            raise ValueError("Error: Input contains invalid character.")

        self.__seq = seq
        self.__transcribe()

    def __transcribe(self):
        self.__seq = self.__seq.replace('T', 'U')

    def get_rna(self):
        return self.__seq
