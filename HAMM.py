class Mutation:
    """ Problem
    Given two strings s and t of equal length, the Hamming distance between s and t,
    denoted dH(s,t), is the number of corresponding symbols that differ in s and t

    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t)

    Sample Dataset
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    Sample Output
    7
    """

    def __init__(self, sequence1, sequence2):
        self.__seq1 = sequence1
        self.__seq2 = sequence2
        self.__mutation = 0
        self.__count_mutation()

    def __count_mutation(self):
        for i, c in enumerate(self.__seq1):
            if c != self.__seq2[i]:
                self.__mutation += 1

    def get_result(self):
        return self.__mutation
