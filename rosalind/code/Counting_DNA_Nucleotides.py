from collections import defaultdict;

def count_dna_nucleotides(dna):
    d = defaultdict(int)
    for c in dna.upper():
        d[c] += 1
    return "%d %d %d %d" % (d['A'], d['C'], d['G'], d['T'])


def test():
    dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    ret = count_dna_nucleotides(dna)
    return ret == "20 12 17 21"
    

if __name__ == '__main__':
    if not test():
        print("count_dna_nucleotides: Failed")

    with open('rosalind_dna.txt') as fh:
        dna = fh.read()
        ret = count_dna_nucleotides(dna)
        print(ret)
