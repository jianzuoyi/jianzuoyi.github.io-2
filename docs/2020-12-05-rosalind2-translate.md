# 生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译

我在[生物信息学：全景](https://zhuanlan.zhihu.com/p/292351855)一文中，阐述了生物信息学的应用领域非常广泛。但是有一点是很关键的，就是细胞内的生命活动都遵从中心法则，生物信息学很多时候就是在中心法则上做文章：

* 分子生物学中心法则：DNA --> RNA --> 蛋白质 --> 细胞表型
* 基因组中心法则：基因组 --> 转录组 --> 蛋白质组 --> 细胞表型

如何用计算机语言描述生物大分子，以及它们之间如何相互转换，是首先要面对的问题。

## 问题描述

中心法则涉及3种生物序列，在计算机中，以字符串的形式表示：

* DNA序列：由4种字母{A, T, G, C}形成单链DNA（其对应链可通过碱基互补配对原则推测出来）；

* RNA序列：由4种字母{A, U, G, C}形成RNA链；

* 蛋白序列：由20种英文字母（除开B, J, O, U, X和Z）组成形成多肽链。

遗传密码是三联体的，有4 x 4 x 4共64种可能，但是只编码20种氨基酸。说明有的密码并不编码氨基酸（终止密码子），而有的多个密码子共同决定一个氨基酸。所谓遗传翻译，就是把三联体密码对应到其代表的氨基酸的过程。

**给定：**一条单链的mRNA序列（最长不超过10kb）。

**需得：**其编码的蛋白质序列。

## 示例数据

```bash
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
```

## 示例结果

```bash
MAMAPRTEINSTRING
```

## Python实现

Translating_RNA_into_Protein.py

```python
import sys

table = {
'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
'UGG':'W','CGG':'R','AGG':'R','GGG':'G'
}


def translate(rna, table):
    n = len(rna)
    amino_acids = ''
    for i in range(0, n, 3):
        codon = rna[i:i+3]
        if codon not in table or table[codon] == "Stop":
            break
        else:
            amino_acids += table[codon]
    return amino_acids

def test():
    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    return translate(rna, table) == 'MAMAPRTEINSTRING'

if __name__ == '__main__':
    if not test():
        print("translate: Failed")
        sys.exit(1)

    with open('rosalind_prot.txt') as fh:
        rna = fh.read()
        amino_acids = translate(rna, table)
        print(amino_acids)
```

* 用一个字典来保存密码子表。Python的字典就是用来保存各种“键=值”对的。
* 习题中的密码子表是很简单的，事实上不同物种，不同细胞器，其密码子表可能不一样。比如起始密码子并不是只有常见的ATG，而终止密码子在生物界也不止三个。`BioPython`中的密码子表搜集得比较全面，是很好的参考。
* 翻译过程中循环的退出条件是：出现错误密码子（只有一个碱基，或两个碱基等），或者遇到终止密码子。

## Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English [alphabet](http://rosalind.info/glossary/alphabet/) (all letters except for B, J, O, U, X, and Z). [Protein strings](http://rosalind.info/glossary/protein-string/) are constructed from these 20 symbols. Henceforth, the term [genetic string](http://rosalind.info/glossary/genetic-string/) will incorporate protein strings along with [DNA strings](http://rosalind.info/glossary/dna-string/) and [RNA strings](http://rosalind.info/glossary/rna-string/).

The [RNA codon table](http://rosalind.info/glossary/rna-codon-table/) dictates the details regarding the encoding of specific codons into the amino acid alphabet.

**Given:** An [RNA string](http://rosalind.info/glossary/rna-string/) corresponding to a strand of mRNA (of length at most 10 [kbp](http://rosalind.info/glossary/kbp/)).

**Return:** The protein string encoded by .

## Sample Dataset

```
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
```

## Sample Output

```
MAMAPRTEINSTRING
```

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录](https://zhuanlan.zhihu.com/p/331607752)

[生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译]()

生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信