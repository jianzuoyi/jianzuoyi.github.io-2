# 生物信息学算法之Python实现|Rosalind刷题笔记：012 排列组合

点突变只能使同一个物种内的个体得到变异，而要产生新物种，则需要更大规模的改变，这就是基因组重排。如果我们比较相邻物种的基因组，会发现它们的染色体之间存在许多共线性区域。这些共线性区域所有可能的排列顺序，可以用数学上的全排列来评估。

如有一个集合{1， 2， ...，n}，而{1，2，3，4，5}就是其中一个排列。该集合中所有长度为n的排列数，则称为该集合的全排列。

**给定：** 一个正整数，代表一个集合的元素个数。

**需得：** 该集合所有排列的总数（全排列），并且给出排列的列表（顺序不限）。

## 示例数据

```bash
3
```

## 示例结果

```bash
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

## Python实现

Enumerating_Gene_Orders.py

```python
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
```

* 全排列的数量，等于序列的长度的阶乘
* 全排列，通过Python的itertools.permutations模块计算

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**

