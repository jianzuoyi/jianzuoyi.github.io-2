一不小心进入了大数据这一朝阳产业，内心还有点小激动呢。怎么回事呢？我什么都不知道啊。先看下表吧。



表 1：DNA碱基对单位

| 碱基对          | 单位     | 缩写 | 例子                   |
| --------------- | -------- | ---- | ---------------------- |
| 1               | 单碱基对 | 1bp  |                        |
| 10<sup>3</sup>  | 千碱基对 | 1kb  | 一般编码基因数量级     |
| 10<sup>6</sup>  | 兆碱基对 | 1Mb  | 一般细菌基因组大小     |
| 10<sup>9</sup>  | 吉碱基对 | 1Gb  | 人类基因组为30亿碱基对 |
| 10<sup>12</sup> | 太碱基对 | 1Tb  |                        |
| 10<sup>15</sup> | 拍碱基对 | 1Pb  |                        |

## 1. DNA的基本单位为什么叫碱基对？

因为DNA是由两条反向互补的链组成的，两条链之间遵循碱基互补配对原则（A与T配对，G与C配对）。知道了一条链的序列，就能推断出另一条链的序列。因此当谈到DNA的一个基本单位时，习惯上叫碱基对（base pair，缩写为bp），意味着它可以代表的是一对碱基，也就是一对核酸。

## 2. 基因组大小是怎么定义的？

人的基因组约有3个G，这3个G严格来说是人的一个细胞中一半DNA的碱基数。因为人是二倍体，共有46条染色体，23条来自于父亲，23条来自于母亲。两者共6个G。因此当谈到一个物种的基因组大小时，指的是其配子（单倍体）中所有DNA的碱基数。有人说人的基因组有6个G，这是不严谨的。

## 3. 为什么说生物信息学是大数据行业？

举几个例子：

（1）科研上测人的基因组，习惯上测30X，也就是每一个碱基测30次，那么30*3G就是90G了。一个项目测5个人的，得到的数据差不多要500G硬盘来装了（不考虑压缩的情况）。处理这些数据，对计算资源的要求可想而知，普通笔记本和台式机肯定不行了，得上服务器。测序公司一年测无数个样本，他们的计算机集群的存储空间都是按多少Pb算的。

（2）肿瘤基因检测为什么现在以panel（也就是一些基因的组合）为主？部分项目上WES（全外显子组，就是一个人的所有基因），几乎没有公司的产品是上全基因组的。首先测太多数据没有必要是一回事，测序成本的考量也是一方面。因为即便2Mb的panel，动辄几千上万X的有效数据要求，测序成本是很可观的。

（3）病原宏基因组测序目前被质疑灵敏度不够，也是因为一个样本测序的数据量太大，要考虑成本问题。

总之，行业现在的策略是，全基因组太大，我就测全外显子组，全外显子也大，我就测大Panel，大Panel也贵，就整个小Panel。做出多样化的产品，满足不同支付能力的客户的需求。

所以，虽然目前获取生命DNA的序列信息非常容易，但考虑到成本，也不是可以任性想怎么测就怎么测的。一方面单个样本的数据量大，其次人群队列（十万人口，百万人口，甚至一国人口）的数据，那就更大了。大到不可承受，只能控制住数据规模，在成本与效益之间寻求平衡。

> 大数据的大，不仅在于规模，还在于复杂。规模大，需要巨大的计算资源；复杂，对从业人员的专业技能要求高。试想几卡车钞票要点，能叫大数据吗？

因此，生物信息学作为利用生物学知识与计算机工具处理大规模且复杂的数据，是真正的大数据。

加油吧，大数据人。