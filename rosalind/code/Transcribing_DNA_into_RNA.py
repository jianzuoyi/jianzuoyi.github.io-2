import sys

def transcript(dna):
    return dna.upper().replace('T', 'U')

def test():
    dna  = 'GATGGAACTTGACTACGTAAATT'
    return transcript(dna) == 'GAUGGAACUUGACUACGUAAAUU'

if __name__ == '__main__':
    if not test():
        print("transcript: Failed")
        sys.exit(1)

    with open('rosalind_rna.txt') as fh:
        dna = fh.read()
        rna = transcript(dna)
        print(rna)
