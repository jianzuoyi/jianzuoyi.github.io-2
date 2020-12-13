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

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**