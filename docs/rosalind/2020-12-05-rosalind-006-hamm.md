# 生物信息学算法之Python实现|Rosalind刷题笔记：006 计算点突变数

汉明距离的定义：对于两条长度相等的字符串来说，汉明距离指的是它们之间不相同的字符数。对于两条DNA，则是它们之间的点突变数目。

**给定：**两条长度相等的DNA序列（不超过1kb）。

**需得：**计算汉明距离。

## 示例数据

```bash
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```

## 示例结果

```bash
7
```

## Python实现

Counting_Point_Mutations.py

```python
import sys

def hamm(s1, s2):
    return sum([a != b for a, b in zip(s1, s2)])

def test():
    s1 = 'GAGCCTACTAACGGGAT'
    s2 = 'CATCGTAATGACGGCCT'
    return hamm(s1, s2) == 7

if __name__ == '__main__':
    if not test():
        print("hamm: Failed")
        sys.exit(1)

    lines = []
    with open('rosalind_hamm.txt') as fh:
        lines = fh.readlines()
    mutations = hamm(lines[0], lines[1])
    print(mutations)
```

汉明距离的计算：

1. zip()函数，将两条序列对应的元素打包成一个个元组；
2. 通过列表展开式判断对应元素是否不同；
3. sum()函数计算不相同的字符数，即为汉明距离。

**[学生信欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，请“点赞”为爱发电，只“收藏”不点赞都是耍流氓。**