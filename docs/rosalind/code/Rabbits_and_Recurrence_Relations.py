import sys


def fib(n, k):
    f = [1] * n
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2] * k
    return f[n-1]

def fib2(n, k):
    return 1 if n < 3 else fib(n-1, k) + fib(n-2, k)*k

def test():
    return fib(5, 3) == 19 and fib2(5, 3) == 19

if __name__ == '__main__':
    if not test():
        print("fib: Failed")
        sys.exit(1)
    print(fib(35, 3))
