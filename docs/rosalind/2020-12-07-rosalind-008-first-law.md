# 生物信息学算法之Python实现|Rosalind刷题笔记：008 孟德尔第一定律

遗传学三大定律是：基因的分离定律、基因的自由组合定律、基因的连锁与交换定律。本题主要考查孟德尔第一定律及概率论基础知识。

**给定：** 三个正整数*k, m, n*，表示一个种群有*k + m + n*个个体：*k*是显性纯合个体数，*m*是杂合个体数，*n*是隐性纯合个体数。

**需得：**两个随机选定的个体交配产生具有显性性状的后代的概率（假定任意两个个体都能交配）。

## 示例数据

```bash
2 2 2
```

## 示例结果

```bash
0.78333
```

## Python实现

Mendel_First_Law.py

```python
import sys

def mendel_first_law(k, m, n):
    t = k + m + n
    p_dom = 1 - m/t * (m-1)/(t-1)*0.25 - n/t * (n-1)/(t-1) - m/t * n/(t-1)
    return round(p_dom, 5)

def test():
    return mendel_first_law(2, 2, 2) == 0.78333

if __name__ == '__main__':
    if not test():
        print("medel_first_law: Failed")
        sys.exit(1)
    print(mendel_first_law(16, 29, 28))
```

解题思路：

1. 基因的分离定律的实质是：等位基因在减数分裂生成配子时随同源染色体的分开而分离，进入不同的配子，独立地随配子遗传给后代；
2. 两个独立事件同时发生的概率，等于两个事件的概率的乘积。

有了上面两点认知，我们就可以来解题了。假定k, m, n的基因型分别是：AA, Aa, aa，t = k + m + n。后代中显性性状有两种基因型：AA，Aa；而隐性性状只有一种基因型：aa。

显然，求隐性性状基因型的概率P(rec)更容易，显性基因型概率P(dom) = 1 - P(rec)。隐性基因型可以通过以下基因型的个体交配获得：

* Aa x Aa

```python
P(aa) = m/t*0.5 * (m-1)/(t-1)*0.5
      = m/t*（m-1)/(t-1)*0.25
```

* aa x aa

```python
P(aa) = n/t * (n-1)/(t-1)
```

* Aa x aa, and aa x Aa

```python
P(aa) = m/t * 0.5 * n/(t-1) + n/t * m/(t-1)*0.5
      = 2 * m/t * 0.5 * n/(t-1)
      = m/t * n/(t-1)
```

**Rosalind刷题计划：**

[生物信息学算法之Python实现|Rosalind刷题笔记：001 碱基统计](https://zhuanlan.zhihu.com/p/330815955)

[生物信息学算法之Python实现|Rosalind刷题笔记：002 中心法则：转录](https://zhuanlan.zhihu.com/p/331607752)

[生物信息学算法之Python实现|Rosalind刷题笔记：003 中心法则：翻译](https://zhuanlan.zhihu.com/p/332215875)

生物信息学算法之Python实现|Rosalind刷题笔记：004 求DNA的反向互补序列

生物信息学算法之Python实现|Rosalind刷题笔记：005 计算GC含量

生物信息学算法之Python实现|Rosalind刷题笔记：006 计算点突变数

生物信息学算法之Python实现|Rosalind刷题笔记：007 兔子问题和递推关系

生物信息学算法之Python实现|Rosalind刷题笔记：008 孟德尔第一定律



觉得内容不错，请点赞、评论或分享给需要的朋友吧！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学生信