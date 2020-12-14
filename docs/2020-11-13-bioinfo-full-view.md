# 生物信息学：全景

生物信息学应用领域非常广泛，从学科划分来说，生物科学、农学、林学、医学等所有涉及生命的领域，都有生物信息学的身影。我们可以从三个视角来总结生物信息学的应用领域。

* 细胞
* 生物体
* 生命之树

## 一、从细胞角度认识生物信息学

细胞内的生命活动遵从中心法则，如下图所示：

![查看源图像](https://huohua-component.huohuaschool.com/20181105/b9ff9318a02ab45708e07e3cf72f85ba.png?x-oss-process=image/resize,m_fill,h_395,w_700)

​                                                                                                                         图片来源于网络，侵删

* 遗传信息从DNA流向RNA，再流向蛋白质。DNA是遗传信息的载体，RNA充当遗传信息的中介，蛋白质是生命活动的具体承担者；

* DNA和RNA都可以自我复制；

* RNA可以通过反转录作用成为DNA；

* 细胞内DNA集合形成基因组，RNA集合形成转录组，蛋白质集合形成蛋白质组，因此中心法则可以分为两个层次：

  1. 分子生物学中心法则

     ```mermaid
     graph LR
     
     DNA  --> RNA --> 蛋白质 --> 细胞表型
     ```

     

  2. 基因组中心法则

```mermaid
graph LR

基因组 --> 转录组 --> 蛋白质组 --> 细胞表型
```

当分子序列数据出现并开始改变传统生物学之时，生物信息学应运而生，其主要任务是聚焦于海量分子序列的分析。而基因组学和功能基因组学为两个紧密关联的学科。基因组学的目标是研究一个生物体的全部DNA序列，即基因组。功能基因组学致力于使用全基因组实验方法来研究基因和蛋白质功能。这体现了生物信息学的本质：生物学问题可以从多个层面来进行研究；从小到单个基因和蛋白质，大到细胞内通路和网络，甚至全基因组应答。我们的目标是利用计算机算法和数据库来助力生命科学的研究。

## 二、从生物体角度认识生物信息学

在细胞之后，认识生物信息学的第二个视角是单个生物体。多细胞生物体在不同发育阶段、不同身体部位或不同的生理状态下都在发生变化，这是因为基因在不同时间和空间、不同生理状态下受到动态调控，基因的表达会动态变化。目前功能基因组学最强大的应用就是使用DNA芯片或RNA测序来测量生物样本中数以千计的基因表达水平。

## 三、从生命之树角度认识生物信息学

认识生物信息学最大的视角是生命之树。现今存活的数百万个物种可以被划分为三大分支：即细菌、古细菌和真核生物（病毒并不完全符合生命的定义）。目前数千种生物的全基因组序列已被公布。从这些信息中我们学到的一个重要信息就是生命分子水平上的根本一致性。这有力地验证了达尔文的进化论，唯有世界上所有生命都起源于一个共同的祖先，才能解释生命分子水平上具有如此的一致性。当前比较基因组学正显示出强大的威力。通过分析DNA序列，我们了解了染色体如何演化，及其如何通过重复、缺失、重排乃至全基因组重复而被塑造。