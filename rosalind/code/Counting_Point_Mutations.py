import sys

def hamm(s1, s2):
    return sum([a != b for a, b in zip(s1, s2)])

def test():
    s1 = 'GAGCCTACTAACGGGAT'
    s2 = 'CATCGTAATGACGGCCT'
    return hamm(s1, s2) == 7

if __name__ == '__main__':
    if not test():
        print("hamm: Failed")
        sys.exit(1)

    lines = []
    with open('rosalind_hamm.txt') as fh:
        lines = fh.readlines()
    mutations = hamm(lines[0], lines[1])
    print(mutations)
