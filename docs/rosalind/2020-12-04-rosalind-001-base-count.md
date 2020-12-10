# 生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计

## 前言

> Rosalind is a platform for learning bioinformatics and programming through problem solving.

Rosalind是一个通过解决实际生物学问题来学习生物信息和练习编程的平台，类似于IT行业的刷题网站力扣（LeetCode）。工作学习之余，咱们也来刷一波吧。

## 说明

* Python是我推荐做生信必学的一门脚本语言，因此所有算法都用Python实现。
* Rosalind刷题需要有一定的Python编程基础。
* 最好在Linux系统下进行编写和测试Python脚本。
* 鉴于Python的哲学是：处理一件事最好的方法只有一种。因此我在解完题后，会参考别人已有的答案，如果解决方式更好，便会采用，同时会注明出处。这样做的目的是力求为读者呈现最佳的解题思路，不会为了原创而原创。
* 英文原问题会附在文章后面。

---

## 问题描述

字符串是Python中的一种基本数据类型，一个字符串由一组有序的字符组成。由于DNA的四种碱基通常用A、T、C、G四个字母表示，因此一段DNA序列可以通过一个字符串表示，如：ATGCTTCAGAAAGGTCTTACG

**给定：**一条长度至多1000bp的DNA字符序列。

**需得：**4个以空格隔开的整数，分别表示4种碱基（A, C, G, T）在字符串中出现的次数。

## 示例数据

```bash
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

## 示例结果

```bash
20 12 17 21
```

## Python实现

Counting_DNA_Nucleotides.py

```python
from collections import defaultdict;

def count_dna_nucleotides(dna):
    d = defaultdict(int)
    for c in dna.upper():
        d[c] += 1
    return "%d %d %d %d" % (d['A'], d['C'], d['G'], d['T'])


def test():
    dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    ret = count_dna_nucleotides(dna)
    return ret == "20 12 17 21"


if __name__ == '__main__':
    if not test():
        print("count_dna_nucleotides: Failed")

    with open('rosalind_dna.txt') as fh:
        dna = fh.read()
        ret = count_dna_nucleotides(dna)
        print(ret)
```

说明：

* 用一个字典保存四种碱基的计数
* 用defaultdict而不是普通的dict，defaultdict的好处是任意键都已经默认初始化了一个值，可以直接使用
* 一个小技巧是构造一个测试函数test()，先用示例数据测试通过后再用从Rosalind下载的数据集进行计算答案，确保一次通过

**怎么样，很简单吧，趁车速还不快，赶快上车吧。**

---

## Problem

A [string](http://rosalind.info/glossary/string/) is simply an ordered collection of symbols selected from some [alphabet](http://rosalind.info/glossary/alphabet/) and formed into a word; the [length](http://rosalind.info/glossary/string-length/) of a string is the number of symbols that it contains.

An example of a length 21 [DNA string](http://rosalind.info/glossary/dna-string/) (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

**Given:** A DNA string of length at most 1000 nt.

**Return:** Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in .

## Sample Dataset

```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

## Sample Output

```
20 12 17 21
```

**下一篇：生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录**



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，或公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学习生信
