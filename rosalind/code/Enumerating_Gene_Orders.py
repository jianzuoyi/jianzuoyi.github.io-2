import sys
import itertools

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def perm(n):
    seq = [str(i+1) for i in range(n)]
    return factorial(n), itertools.permutations(seq, n)

def test():
    return perm(3)[0] == 6

if __name__ == '__main__':
    if not test():
        print("perm: Failed")
        sys.exit(1)
    n, p = perm(7)
    print(n)
    for i in p:
        print(" ".join(i))
