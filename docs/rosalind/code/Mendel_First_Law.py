import sys

def mendel_first_law(k, m, n):
    t = k + m + n
    p_dom = 1 - m/t * (m-1)/(t-1)*0.25 - n/t * (n-1)/(t-1) - m/t * n/(t-1)
    return round(p_dom, 5)

def test():
    return mendel_first_law(2, 2, 2) == 0.78333

if __name__ == '__main__':
    if not test():
        print("medel_first_law: Failed")
        sys.exit(1)
    print(mendel_first_law(16, 29, 28))
