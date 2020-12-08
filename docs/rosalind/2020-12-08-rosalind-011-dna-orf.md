# 生物信息学算法之Python实现|Rosalind刷题笔记：011 DNA六框翻译

开放阅读框（Open Reading Frame, ORF）是由起始密码子开始，直到终止密码子结束，中间不含有其他终止密码子的核酸序列。

由于DNA是双链结构，任何一条链都可以作为模板合成RNA；并且又因为遗传密码是三联体，由三个核苷酸决定一个氨基酸，因此对于一段DNA序列，有六种可能的阅读框（正向三个，反向三个）。通常情况下，六种阅读框只有一种是正确的：一般是翻译得到最长氨基酸序列的阅读框。

**给定：** Fasta文件中一条长度不超过1kb的DNA序列。

**需得：** 不同的由ORF翻译而来的蛋白序列。返回翻译的蛋白序列时可以是任意顺序。

## 示例数据

```bash
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

## 示例结果

```bash
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
```

## Python实现

Open_Reading_Frames.py

```python
import sys
import pysam
table = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""
table = dict(zip(table.split()[::2],table.split()[1::2]))

def translate(dna):
    aa = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if table[codon] == 'Stop':
            break
        aa += table[dna[i:i+3]]
    return aa

def reverse_complement(dna):
    revc = ""
    basepair = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for c in dna:
        revc = basepair[c] + revc
    return revc

def find_orf(dna):
    ret = []
    dna_len = int(len(dna)/3) * 3
    i = 0
    for i in range(0, dna_len, 3):
        codon = dna[i:i+3]
        if codon != 'ATG': continue
        base = codon
        for j in range(i+3, dna_len, 3):
            codon = dna[j:j+3]
            base += codon
            if table[codon] == 'Stop':
                ret.append(base)
                break
    return ret

def six_frame_translate(dna):
    revc = reverse_complement(dna)
    amino_acids = []
    for i in range(3):
        for orf in find_orf(dna[i:]) + find_orf(revc[i:]):
            if orf:
                amino_acids.append(translate(orf))
    return set(amino_acids)

def test():
   dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
   return 'MLLGSFRLIPKETLIQVAGSSPCNLS' in six_frame_translate(dna)


if __name__ == '__main__':
    if not test():
        print("six_frame_translate: Failed")
        sys.exit(1)

    with pysam.FastxFile('rosalind_orf.txt') as fh:
        for r in fh:
            six = six_frame_translate(r.sequence)
            print("\n".join(six))
```

* 六框翻译，即正向三次，反向三次
* 由于允许ORF重叠，因此本题的关键是要找到所有的ORF（find_orf函数，使用了双层循环，第一层找起始密码子，第二层找终止密码子）
* 逐个翻译每个ORF（translate函数），最后用set()函数去除冗余

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录](https://zhuanlan.zhihu.com/p/331607752)

[生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译](https://zhuanlan.zhihu.com/p/332215875)

生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列

生物信息学算法之Python实现|Rosalind刷题笔记：005 计算GC含量

生物信息学算法之Python实现|Rosalind刷题笔记：006 计算点突变数

生物信息学算法之Python实现|Rosalind刷题笔记：007 兔子问题和递推关系

生物信息学算法之Python实现|Rosalind刷题笔记：008 孟德尔第一定律

生物信息学算法之Python实现|Rosalind刷题笔记：009 查找DNA中的motif

生物信息学算法之Python实现|Rosalind刷题笔记：010 DNA一致性序列计算

生物信息学算法之Python实现|Rosalind刷题笔记：011 DNA六框翻译



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信

