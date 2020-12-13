# 生物信息学算法之Python实现|Rosalind刷题笔记：013 随机DNA序列

众所周知，基因组的核酸链不可能是随机形成的。有时候许多物种基因组之间，存在一些保守序列（motif），这意味着它们可能具有重要功能。但是，我们如何确定这些序列不是随机形成的DNA片段呢？

一个常识是：越短的序列越容易随机形成，越长的序列越难随机形成。如何对随机形成序列的概率进行量化，以及如何确定容易和不容易随机形成的序列的长度的阈值呢？这篇文章将对这个问题进行探索。

**给定：** 一段DNA序列，以及一系列假定的GC出现的概率。

**需得：** 在特定GC出现的概率的情况下，得到一条与给定DNA序列GC含量相同的序列的概率，并且将概率值取对数输出。

## 示例数据

```bash
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
```

## 示例结果

```bash
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
```

## Python实现

> 本题思路参考自下述博客：
>
> [Rosalind – Introduction to Random Strings](https://recologia.com.br/2016/06/08/rosalind-introduction-to-random-strings/)

因为DNA有4种碱基，每一个位置都有4种可能。如果每一种碱基出现的概率都是25%，那么一个9bp的序列，共有4·4·4·4·4·4·4·4·4 = 4<sup>9</sup>=262144种可能性。但现在我们假定GC出现的概率是0.129而不是0.5，那么1-0.129，即0.871就是A或T出现的概率。在此情况下，现在计算一个分子有多大概率得到与所给序列相同的GC含量？

```python
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
```

下面我们在Python中演示如何计算。

```bash
dna = 'ACGATACAA'
A = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'
prob_gc = map(float, A.split())
```

由于G、C单独出现的概率是GC同时出现的概率的一半，A、T单独出现的概率是AT同时出现的概率的一半；又由于每一种碱基都是独立出现的，因此一条序列出现的概率是所有碱基分别出现的概率之乘积。

```bash
总的概率值 = 第1个碱基的概率 * 第2个碱基的概率 ……*最后一个碱基的概率

```

用代码表示就是：

```python
gc = 0.129
at = 1 - 0.129
prob = 1.0
for base in dna:
    if base in 'GC':
        prob *= gc*0.5
    else:
        prob *= at*0.5
```

由于概率值都小于1，多个概率值相乘，结果会越来越小，不如对结果取对数，以方便表示。

```python
print(log10(prob))
```

又因为对数具有如下特性：

```python
log(x·y) = log(x) + log(y)
```

因此，可以修改上面的代码：

```python
gc = 0.129
at = 1 - gc
prob = 0.0
for base in dna:
    if base in 'GC':
        prob += log10(gc*0.5)
    else:
        prob += log10(at*0.5)
```

上面的代码也等价于：

```python
gc = 0.129
at = 1 - gc
gc_num = dna.count('G') + dna.count('C')
at_num = len(dna) - gc_num
prob = gc_num * log10(gc*0.5) + at_num * log10(at*0.5)
```

完整的代码是：

Introduction_to_Random_Strings.py

```python
import sys
from math import log10

#dna = 'ACGATACAA'
#A = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'

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
```

注意：

* 我们计算概率的序列，只是GC含量与给定序列相同，并没有考虑碱基顺序；
* 由结果可知：当GC出现概率与给定DNA的GC含量相同时，出现与给定DNA的GC含量相同的序列的概率最大。

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**

