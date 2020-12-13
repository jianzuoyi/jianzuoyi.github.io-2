import sys
import pysam

def consensus(infasta):
    # Create profile matrix
    base = 'ACGT'
    profile = [] 
    with pysam.FastxFile(infasta) as fh:
        for r in fh:
            if not profile:
                profile = [[0] * len(r.sequence) for x in base]
            for i,b in enumerate(r.sequence):
                profile[base.index(b)][i] += 1

    # Get consensus string
    cons = ''
    for i in range(len(profile[0])):
        count = { b:profile[base.index(b)][i] for b in base }
        cons += max(count.items(), key=lambda x: x[1])[0]
    return cons, profile

def test():
    cons, profile = consensus('rosalind_cons_test.txt')
    cons, profile = consensus('rosalind_cons.txt')
    print(cons)
    for i,base in enumerate('ACGT'):
        line = ' '.join(['%s:'%base] + [str(n) for n in profile[i]])
        print(line)
    return cons == 'ATGCAACT'

if __name__ == '__main__':
    test()
