import sys
import pysam

def gc_content(item):
    n, s = item
    return (s.count('G') + s.count('C')) * 100 / len(s)

def max_gc_content(infasta):
    dna = {}
    with pysam.FastxFile(infasta) as fh:
        for r in fh:
            dna[r.name] = r.sequence.upper()
    return max(dna.items(), key=gc_content)

def test():
    item = max_gc_content('rosalind_gc_test.txt')
    return item[0] == 'Rosalind_0808' and round(gc_content(item), 6)== 60.919540

if __name__ == '__main__':
    if not test():
        print("cout_gc_content:Failed")
        sys.exit(1)

    item = max_gc_content('rosalind_gc.txt')
    print(item[0])
    print(gc_content(item))
