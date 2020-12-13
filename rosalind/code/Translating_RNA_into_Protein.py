import sys

table = {
'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
}


def translate(rna, table):
    n = len(rna)
    amino_acids = ''
    for i in range(0, n, 3):
        codon = rna[i:i+3]
        if codon not in table or table[codon] == "Stop":
            break
        else:
            amino_acids += table[codon]
    return amino_acids

def test():
    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    return translate(rna, table) == 'MAMAPRTEINSTRING'

if __name__ == '__main__':
    if not test():
        print("translate: Failed")
        sys.exit(1)

    with open('rosalind_prot.txt') as fh:
        rna = fh.read()
        amino_acids = translate(rna, table)
        print(amino_acids)
