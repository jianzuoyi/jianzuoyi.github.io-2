import sys
import pysam
table = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""
table = dict(zip(table.split()[::2],table.split()[1::2]))

def translate(dna):
    aa = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if table[codon] == 'Stop':
            break
        aa += table[dna[i:i+3]]
    return aa

def reverse_complement(dna):
    revc = ""
    basepair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for c in dna:
        revc = basepair[c] + revc
    return revc

def find_orf(dna):
    ret = []
    dna_len = int(len(dna)/3) * 3
    i = 0
    for i in range(0, dna_len, 3):
        codon = dna[i:i+3]
        if codon != 'ATG': continue
        base = codon
        for j in range(i+3, dna_len, 3):
            codon = dna[j:j+3]
            base += codon
            #print(i, j, codon)
            if table[codon] == 'Stop':
                ret.append(base)
                break
    return ret

def six_frame_translate(dna):
    revc = reverse_complement(dna)
    amino_acids = []
    for i in range(3):
        for orf in find_orf(dna[i:]) + find_orf(revc[i:]):
            if orf:
                amino_acids.append(translate(orf))
    return set(amino_acids)

def test():
   dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
   return 'MLLGSFRLIPKETLIQVAGSSPCNLS' in six_frame_translate(dna)
   

if __name__ == '__main__':
    if not test():
        print("six_frame_translate: Failed")
        sys.exit(1)

    with pysam.FastxFile('rosalind_orf.txt') as fh:
        for r in fh:
            six = six_frame_translate(r.sequence)
            print("\n".join(six))
