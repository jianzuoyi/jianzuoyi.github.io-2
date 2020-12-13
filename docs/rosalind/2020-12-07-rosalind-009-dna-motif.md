# 生物信息学算法之Python实现|Rosalind刷题笔记：009 查找DNA中的motif

在字符串中查找子串是一个常见问题。子串在字符串中可能是唯一的，比如特定的基因序列；也有可能有多个拷贝，比如基因组中的重复序列。这些重复序列可能相同，可能有微小区别。本题中重复子串完全相同，可以简单地通过Python的`find()`函数来查找，如果重复子串不完全相同并且符合某种模式，则可以用正则表达式模块`re`来处理。

**给定：** 两个DNA序列*s*和*t*（长度都不超过1kb）。

**需得：** *t*在*s*中的所有位置。

## 示例数据

```bash
GATATATGCATATACTT
ATAT
```

## 示例结果

```bash
2 4 10
```

## Python实现

Finding_a_Motif_in_DNA.py

```python
import sys
import re

def find_motif(s, t):
    ret = []
    pos = s.find(t)
    while pos != -1:
        ret.append(pos+1)
        pos = s.find(t, pos+1)
    return ' '.join([str(n) for n in ret])

def test():
    return find_motif('GATATATGCATATACTT', 'ATAT') == '2 4 10'

if __name__ == '__main__':
    if not test():
        print("find_motif: Failed")
        sys.exit(1)

    with open('rosalind_subs.txt') as fh:
        s = fh.readline().rstrip()
        t = fh.readline().rstrip()
        print(find_motif(s, t))
```

* 注意找到一个位置后，再次查找需要从下一个位置（pos+1）开始，以防止重复查找。

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**

