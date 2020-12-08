import sys
import re

def find_motif(s, t):
    ret = []
    pos = s.find(t)
    while pos != -1:
        ret.append(pos+1)
        pos = s.find(t, pos+1)
    return ' '.join([str(n) for n in ret])

def test():
    return find_motif('GATATATGCATATACTT', 'ATAT') == '2 4 10'

if __name__ == '__main__':
    if not test():
        print("find_motif: Failed")
        sys.exit(1)

    with open('rosalind_subs.txt') as fh:
        s = fh.readline().rstrip()
        t = fh.readline().rstrip()
        print(find_motif(s, t))
