import re


class Motif:
    """ Problem: Finding a Motif in DNA
    Given two strings s and t, t is a substring of s if t is contained as a contiguous
    collection of symbols in s (as a result, t must be no longer than s).

    The position of a symbol in a string is the total number of symbols found to its left,
    including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG"
    are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

    A substring of s can be represented as s[j:k], where j and k represent the starting and
    ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG",
    then s[2:5] = "UGCU".

    The location of a substring s[j:k] is its beginning position j; note that t will have
    multiple locations in s if it occurs more than once as a substring of s

    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.

    Sample Dataset
    GATATATGCATATACTT
    ATAT
    Sample Output
    2 4 10
    """

    def __init__(self, sequence, motif):
        self.__seq = sequence
        self.__motif = motif
        self.__loc = list()
        self.__find_motif()

    def __find_motif(self):
        """
        Regular expression
        https://docs.python.org/3.9/library/re.html
        (?=...)
        Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.

        re.finditer(pattern, string, flags=0)
        Return an iterator yielding match objects over all non-overlapping matches for the RE pattern in string.
        The string is scanned left-to-right, and matches are returned in the order found.
        Empty matches are included in the result.
        """
        self.__loc = [s.start() + 1 for s in re.finditer(f'(?={self.__motif})', self.__seq)]

    def get_result(self):
        return self.__loc
