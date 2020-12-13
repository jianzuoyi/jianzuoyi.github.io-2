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

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**