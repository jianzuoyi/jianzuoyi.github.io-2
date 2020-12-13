import sys
from math import log10

dna = 'ACGATACAA'
A = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'

with open('rosalind_prob.txt') as fh:
    dna, A = [l.strip() for l in fh.readlines()]
gc_prob = map(float, A.split())
gc_num = dna.count('G') + dna.count('C')
at_num = len(dna) - gc_num

B = []
for gc in gc_prob:
    at = 1 - gc
    p = gc_num * log10(gc*0.5) + at_num * log10(at*0.5)
    B.append(p)

print(' '.join([str(round(i, 3)) for i in B]))
