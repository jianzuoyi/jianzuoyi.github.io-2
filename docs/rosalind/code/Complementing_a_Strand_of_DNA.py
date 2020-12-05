import sys

def reverse_complement(dna):
    revc = ""
    basepair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for c in dna:
        revc = basepair[c] + revc
    return revc

def test():
    dna = 'AAAACCCGGT'
    return reverse_complement(dna) == 'ACCGGGTTTT'

if __name__ == '__main__':
    if not test():
        print("reverse_complement: Failed")
        sys.exit(1)

    with open('rosalind_revc.txt') as fh:
        dna = fh.read()
        revc = reverse_complement(dna.strip().upper())
        print(revc)
