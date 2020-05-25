import os


class GCContent:
    """ Problem: Computing GC Content

    The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
    For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string
    has the same GC-content. DNA strings must be labeled when they are consolidated into a database. A
    commonly used method of string labeling is called FASTA format. In this format, the string is introduced
    by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string
    itself; the first line to begin with '>' indicates the label of the next string.
    In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx",
    where "xxxx" denotes a four-digit code between 0000 and 9999.

    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
    Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
    please see the note on absolute error below.

    Sample Dataset
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
    Sample Output
    Rosalind_0808
    60.919540

    """
    __precision = 6

    def __init__(self, filepath):
        if not os.path.isfile(filepath):
            raise ValueError(f"Error: File path '{filepath}' does not exist.")
        self.__file = filepath
        self.__store = dict()
        self.__gc()

    def __gc(self):
        total = 0
        gc = 0
        name = ""
        with open(self.__file) as file:
            for line in file:
                if line.startswith(">"):
                    if gc != 0:
                        percent = gc / total * 100
                        self.__store.update({name: round(percent, GCContent.__precision)})
                    name = line[1:-1]
                    total = 0
                    gc = 0
                else:
                    line = line[:-1]
                    total += len(line)
                    gc += line.count('G') + line.count('C')
            percent = gc / total * 100
            self.__store.update({name: round(percent, GCContent.__precision)})

    def get_result(self):
        a = max(self.__store, key=self.__store.get)
        b = self.__store[a]
        return [a, b]
