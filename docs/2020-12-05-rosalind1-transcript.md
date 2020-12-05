# 生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录

我在[生物信息学：全景](https://zhuanlan.zhihu.com/p/292351855)一文中，阐述了生物信息学的应用领域非常广泛。但是有一点是很关键的，就是细胞内的生命活动都遵从中心法则，生物信息学很多时候就是在中心法则上做文章：

* 分子生物学中心法则：DNA --> RNA --> 蛋白质 --> 细胞表型
* 基因组中心法则：基因组 --> 转录组 --> 蛋白质组 --> 细胞表型

如何用计算机语言描述生物大分子，以及它们之间如何相互转换，是首先要面对的问题。

---

## 问题描述

遗传信息从DNA流向RNA的过程，称为转录。DNA有4张不同的扑克牌，RNA也有4张，唯一的区别是DNA中的T，在RNA中变成了U，因此RNA的4张牌是：A、U、C、G。因此，给定一条与编码链相同的DNA序列，要转录成RNA只需要将T替换成U就可以了。

**给定**：一条长度至多1000bp的DNA序列。

**需得：**其转录的RNA序列。

## 示例数据

```bash
GATGGAACTTGACTACGTAAATT
```

## 示例结果

```bash
GAUGGAACUUGACUACGUAAAUU
```

## Python实现

Transcribing_DNA_into_RNA.py

```python
import sys

def transcript(dna):
    return dna.upper().replace('T', 'U')

def test():
    dna  = 'GATGGAACTTGACTACGTAAATT'
    return transcript(dna) == 'GAUGGAACUUGACUACGUAAAUU'

if __name__ == '__main__':
    if not test():
        print("transcript: Failed")
        sys.exit(1)

    with open('rosalind_rna.txt') as fh:
        dna = fh.read()
        rna = transcript(dna)
        print(rna)
```

* 只需要将`T`替换成`U`就可以了；替换前先用upper()是为了提高程序的健壮性，使得输入序列中含有小写字母时也能转换成功。

---

## Problem

An [RNA string](http://rosalind.info/glossary/rna-string/) is a [string](http://rosalind.info/glossary/string/) formed from the [alphabet](http://rosalind.info/glossary/alphabet/) containing 'A', 'C', 'G', and 'U'.

Given a [DNA string](http://rosalind.info/glossary/dna-string/) corresponding to a coding strand, its transcribed [RNA string](http://rosalind.info/glossary/rna-string/) is formed by replacing all occurrences of 'T' in with 'U' in .

**Given:** A [DNA string](http://rosalind.info/glossary/dna-string/) having [length](http://rosalind.info/glossary/string-length/) at most 1000 [nt](http://rosalind.info/glossary/nucleotide/).

**Return:** The transcribed RNA string of .

## Sample Dataset

```
GATGGAACTTGACTACGTAAATT
```

## Sample Output

```
GAUGGAACUUGACUACGUAAAUU
```

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录]()

生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信