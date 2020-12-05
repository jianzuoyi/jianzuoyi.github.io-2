# 生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列

碱基互补配对原则是：A与T配对，G与C配对。

求DNA的反向互补序列分两步：第一是反向，第二是互补。比如序列“ATGC”，反向就是“CGTA”，再互补就是“GCAT”。

**给定：**长度不超过1000bp的DNA序列。

**需得：**其反向互补序列。

## 示例数据

```bash
AAAACCCGGT
```

## 示例结果

```bash
ACCGGGTTTT
```

## Python实现

Complementing_a_Strand_of_DNA.py

```python
import sys

def reverse_complement(dna):
    revc = ""
    basepair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for c in dna:
        revc = basepair[c] + revc
    return revc

def test():
    dna = 'AAAACCCGGT'
    return reverse_complement(dna) == 'ACCGGGTTTT'

if __name__ == '__main__':
    if not test():
        print("reverse_complement: Failed")
        sys.exit(1)

    with open('rosalind_revc.txt') as fh:
        dna = fh.read()
        revc = reverse_complement(dna.strip().upper())
        print(revc)
```

* 在Python中，是没有switch语句的，可以用if...elif...elif..else来模拟switch语句；而更pythonic的做法是用字典来代替。在本题中，你可以尝试用if...elif...else来实现反向互补。
* Python中的序列反向可以通过切片实现，如dna_forward[::-1]，就得到了其反向序列，再求其互补序列，也可以实现反向互补的需求。

## Problem

In [DNA strings](http://rosalind.info/glossary/dna-string/), [symbols](http://rosalind.info/glossary/symbol/) 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The [reverse complement](http://rosalind.info/glossary/reverse-complement/) of a [DNA string](http://rosalind.info/glossary/dna-string/) is the string formed by reversing the symbols of , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

**Given:** A DNA string of length at most 1000 [bp](http://rosalind.info/glossary/base-pair/).

**Return:** The reverse complement of .

## Sample Dataset

```
AAAACCCGGT
```

## Sample Output

```
ACCGGGTTTT
```

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录](https://zhuanlan.zhihu.com/p/331607752)

[生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译]()

生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信