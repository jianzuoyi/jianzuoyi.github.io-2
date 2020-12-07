# 生物信息学算法之Python实现|Rosalind刷题笔记：005 计算GC含量

DNA序列的GC含量是指序列中'G'和'C'所占的百分比。

一条DNA序列很容易表示，但是如果有多条DNA序列放在一起，则每条序列必须被标记，通常的做法是保存为FASTA格式文件。在这种格式中，序列的名称占一行，名称的最前面是一个大于符号‘>’开头，序列名称后面可以跟一系列说明；序列信息从名称的下一行开始，直到遇到下一个以‘>’开头的序列名称为止。Fasta格式文件可参考下面的示例数据。

**给定：**一个Fasta序列文件。

**需得：**GC含量最高的序列名称及其GC含量（各占一行行输出）。

## 示例数据

```bash
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

## 示例结果

```bash
Rosalind_0808
60.919540
```

## Python实现

Computing_GC_Content.py

```python
import sys
import pysam

def gc_content(item):
    n, s = item
    return (s.count('G') + s.count('C')) * 100 / len(s)

def max_gc_content(infasta):
    dna = {}
    with pysam.FastxFile(infasta) as fh:
        for r in fh:
            dna[r.name] = r.sequence.upper()
    return max(dna.items(), key=gc_content)

def test():
    item = max_gc_content('rosalind_gc_test.txt')
    return item[0] == 'Rosalind_0808' and round(gc_content(item), 6)== 60.919540

if __name__ == '__main__':
    if not test():
        print("cout_gc_content:Failed")
        sys.exit(1)

    item = max_gc_content('rosalind_gc.txt')
    print(item[0])
    print(gc_content(item))
```

本题要点：

1. 用pysam读取Fasta文件，并将其放入字典中；详细用法见：[基因组文件读写（pysam）](https://zhuanlan.zhihu.com/p/297858072)
2. max函数的使用，特别是为其构造一个key函数并传入，这是解本题的关键，GC含量本身是很容易理解的。

## Problem

The GC-content of a [DNA string](http://rosalind.info/glossary/dna-string/) is given by the percentage of [symbols](http://rosalind.info/glossary/symbol/) in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the [reverse complement](http://rosalind.info/glossary/reverse-complement/) of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called [FASTA format](http://rosalind.info/glossary/fasta-format/). In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

**Given:** At most 10 [DNA strings](http://rosalind.info/glossary/dna-string/) in FASTA format (of length at most 1 [kbp](http://rosalind.info/glossary/kbp/) each).

**Return:** The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on [absolute error](http://rosalind.info/glossary/absolute-error/) below.

## Sample Dataset

```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

## Sample Output

```
Rosalind_0808
60.919540
```

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录](https://zhuanlan.zhihu.com/p/331607752)

[生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译]()

生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列

生物信息学算法之Python实现|Rosalind刷题笔记：005 计算GC含量



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信
