# 从零开始学PCR技术（五）：试验污染

PCR反应最大的特点是具有较大的扩增能力和极高的灵敏度，正因为如此，极其微量的污染即可造成检测结果的假阳性。监控污染，防止污染对检测结果的影响，不仅对实验，对后续生信分析也提出了挑战。

## 一、污染原因

### 1. 交叉污染

(1) 容器被污染。

(2) 标本放置时，由于密封不严溢于容器外。

(3) 容器外粘有标本而造成相互间交叉污染。

(4) 标本核酸模板在提取过程中，由于吸样枪污染导致标本间污染。

(5) 有些微生物标本尤其是病毒可随气溶胶或形成气溶胶而扩散，导致彼此间的污染。

### 2. 试剂污染

PCR试剂配制过程中，由于加样枪、容器、双蒸水及其它溶液被PCR核酸模板污染。

### 3. 扩增产物污染

这是PCR污染最主要的形式，因为：

(1) PCR产物拷贝量大（一般为10<sup>^</sup>13拷贝/ml），远远高于PCR检测数个拷贝的极限，所以极微量的PCR产物污染，就可形成假阳性。

(2) 最有可能造成PCR产物污染的形式是气溶胶污染。在空气与液体面摩擦时就可形成气溶胶，在操作时比较剧烈地摇动反应管，开盖时、吸样时及污染进样枪的反复吸样都可形成气溶胶而污染。据计算一个气溶胶颗粒可含48000拷贝，因而由其造成的污染是一个值得特别重视的问题。

### 4. 克隆质粒污染

(1) 某些用克隆质粒做阳性对照的检验室，这个问题比较常见。

(2) 克隆质粒在单位容积内含量相当高，另外在纯化过程中需用较多的用具及试剂，而且在活细胞内的质粒，由于活细胞的生长繁殖的简便性及具有很强的生命力，其污染可能性也很大。

## 二、污染监测

通常使用对照对检测的各个环节进行监控，常用的对照有以下这些。

### (一) PCR中的对照

#### 1. 阳性对照与阴性对照

阳性对照和阴性对照是指在相同的处理条件下，比如一份已知的感染样品和一份已知的未感染样品，都进行了提取和扩增最终获得了阳性结果和阴性结果。阴阳性对照强调处理过程与样品一致，并且有明确的预期结果。

#### 2. 扩增对照

我们通常说的阳性对照和阴性对照指的是扩增试剂盒中附带的不需要提取的阳性对照和阴性对照，更准确的定义应该是扩增阳性对照和扩增阴性对照。扩增阳性对照含有阳性扩增模板，扩增阴性对照应含有阴性扩增模板（基质核酸）。扩增对照只能监控每次扩增过程中的扩增系统是否正常，不能监控采样、提取和每份样品的操作过程。如果是检测 RNA 样品的检测试剂盒，其扩增阳性对照使用质粒，便无法监控反转录过程。

####  3. 内标（Internal Control, IC）

内标是指在同一反应管中与靶序列共同扩增的一段非靶序列分子。内标有两种形式，一种是使用天然样品中含有的内参基因作为内标，另一种是人工添加的内标。内标的最大特点是与靶序列共同扩增，而其他的对照都是独立扩增。

(1) 内参基因

通常它们在各组织和细胞中的表达相对恒定，在检测基因的表达水平变化时常用它来做参照物。内参基因通常是管家基因（house-keeping gene）因为其表达水平受环境因素影响较小，而且在个体各个生长阶段的几乎全部组织中持续表达变化很小。常用的内参基因包括 GAPDH、β-actin (BETA-actin)、18sRNA、B2M、HPRT 和 TBP 等。

内参基因的优点是与样品中的靶基因经历完全相同的处理程序，可以监控采样，运输，核酸提取和扩增的全部过程。缺点是不同物种，不同生理状态下，不同组织中的内参基因存在一定的差异。如果样品类型是口腔液，咽拭子等样品，内参基因的量很低可能导致实验不成功。如果检测的是环境样品则内参基因可能完全失效。

(2) 人工内标

添加一种不会干扰靶序列扩增的人工合成的内标。现在国外的诊断试剂盒大部分都会将内标直接添加在反应液中与模板一起扩增，但是这样的内标不能监控采样，运输和核酸提取的过程。

还有另一种形式的内标，使用人工合成的假病毒，在核酸提取前在每一份样品中加入等量的内标，这样就可以监控样品的提取到扩增的过程。但是由于是人工添加到样品中，仍然不能监控胞内细菌病毒的释放情况。

####  4. 核酸提取对照

可以使用内参基因，假病毒混合基质，灭活病毒混合基质来监控提取到扩增的流程。

#### 5. 反转录对照（RT control）

可以使用提取好的 RNA 内参基因，RNA 假病毒混合基质，灭活 RNA 病毒混合基质来监控反转录到扩增的流程。

无反转录对照（no-RT control）含有除反转录酶以外的所有成分。

#### 6. 空白对照

(1) 无模板空白对照

NTC （No Template Control）是指不含有模板（阳性模板或者阴性模板），但含有引物探针和反应液，主要监控引物探针、反应体系有没有被污染的对照。目前的试剂盒的 NC 一般都是水或阴性缓冲液，所以 NC 等同于 NTC。其实两者有不同的作用。

(2) 仪器空白对照

仪器空白对照通常使用的是空反应管来监控仪器有无非特异性的荧光信号。

(3) 荧光染料对照

最常使用的是 ROX 染料，由于荧光定量 PCR 的荧光信号在每个样品孔会有微小的差异所以使用特定的 ROX 荧光染料，系统可以根据 ROX 荧光染料的信号值来校准每孔的荧光信号。

#### 7. 质控品（Quality control, QC）

上述环节中使用的各种对照大部分是试剂厂家匹配试剂盒使用的产品，有的是实验室自制，所以整个的监控过程可能存在不够客观和独立。因此在实验室的对照设置中每次检测都建议使用第三方质控品，有条件的使用国家有证标准物质 (Reference material ,RM)。由于标准物质具有准确量值和计量溯源性，可以更准确的评估整个试验流程的准确度。

#### 8. 定值参考品

医学上的定量检测试剂盒，需要配套定值参考品用于试剂盒的定量检测使用。

### (二) PCR对照的选择

从上文可知没有一种对照是完美的，在检测中我们要根据自己的需求来进行灵活选择和搭配。笔者建议每一次检测时添加一个能对从提取到扩增环节进行监控的质控品或标准物质；每份检测样品中添加内标（如果样品种类比较多样建议使用人工内标，如果样品类型为相对固定的动物组织建议使用内参基因）；扩增阳性对照，扩增阴性对照，无模板对照和 ROX 对照。有条件的添加临床阳性对照和临床阴性对照，在怀疑提取环节或者反转录环节出现问题时使用核酸提取对照和反转录对照。不定期使用仪器空白对照。

#### 1. 阳性对照与污染

不可否认的一个事实是阳性对照可以增加实验室污染的风险。这种污染的来源一种是直接来源于扩增阳性对照的污染。对于扩增阳性对照来说通常 10000 拷贝 / 微升（CT 值约 25）是比较理想的，但是有一些试剂盒厂家的扩增阳性对照设置在 CT 值 20 以下，比大部分阳性样本都强。这么高浓度的对照给实验室带来了巨大的污染风险，原因可能仅仅是因为试剂厂家担心其阳性对照不稳定，长时间存放阳性对照降解。另一种污染来自于扩增产物的处理不当，或者实验室的设计布局不合理。

#### 2. 初筛和确诊

对于初筛实验，我们希望提高真阳性检出率，即提高诊断敏感性。我们需要检测系统达到最高检测效率，因此要在不同环节添加阳性对照，确保每个环节的检测效率最高。

对于确诊实验，我们希望提高真阴性检出率，即提高诊断特异性。我们需要确保检测系统不出现假阳性，因此要在不同环节添加阴性对照，减少非必须的阳性对照，甚至要在样品盘的不同位置中随机插入几个阴性对照，确保实验过程中没有被污染。

## 三、污染预防

### 1. 首要原则

(1) 永远要设置NTC对照：如果不能在污染出现的第一时间发现，会导致严重后果：一大段时间的数据不可信。

(2) 准备PCR的移液器要专用：千万不能用吸取PCR产物/克隆质粒的移液器去准备PCR体系。

### 2. 基本策略

#### 2.1 划分操作区

目前，普通PCR尚不能做到单人单管，实现完全闭管操作，但无论是否能够达到单人单管，均要求实验操作在三个不同的区域内进行，PCR的前处理和后处理要在不同的隔离区内进行。

(1) 标本处理区，包括扩增摸板的制备。

(2) 扩增区，包括反应液的配制和PCR扩增。

(3) 产物分析区，凝胶电泳分析，产物拍照及重组克隆的制备。

(4) 各工作区要有一定的隔离，操作器材专用，要有一定的方向性。如：标本制备→PCR扩增→产物分析→产物处理。

切记：产物分析区的产物及器材不要拿到其他两个工作区。

#### 2.2 分装试剂

PCR扩增所需要的试剂均应在装有紫外灯的超净工作台或负压工作台配制和分装。所有的加样器和吸头需固定放于其中，不能用来吸取扩增后的DNA和其他来源的DNA。

(1) PCR用水应为高压的双蒸水。

(2) 引物和dNTP用高压的双蒸水在无PCR扩增产物区配制。

(3) 引物和dNTP应分装储存，分装时应标明时间，以备发生污染时查找原因。

#### 2.3 实验操作注意事项

尽管扩增序列的残留污染大部分是假阳性反应的原因，样品间的交叉污染也是原因之一。因此，不仅要在进行扩增反应时谨慎认真，在样品的收集、抽提和扩增的所有环节都应该注意。

(1) 戴一次性手套，若不小心溅上反应液，立即更换手套。

(2) 使用一次性吸头，严禁与PCR产物分析室的吸头混用，吸头不要长时间暴露于空气中，避免气溶胶的污染。

(3) 避免反应液飞溅，打开反应管时为避免此种情况，开盖前稍离心收集液体于管底。若不小心溅到手套或桌面上，应立刻更换手套并用稀酸擦拭桌面。

(4) 操作多份样品时，制备反应混合液，先将dNTP、缓冲液、引物和酶混合好，然后分装，这样即可以减少操作，避免污染，又可以增加反应的精确度。

(5) 最后加入反应模板，加入后盖紧反应管。

(6) 操作时设立阴阳性对照和空白对照，既可验证PCR反应的可靠性，又可以协助判断扩增系统的可信性。

(7) 尽可能用可替换或可高压处理的加样器，由于加样器最容易受产物气溶胶或标本DNA的污染，最好使用可替换或高压处理的加样器。如没有这种特殊的加样器，至少PCR操作过程中加样器应该专用，不能交叉使用，尤其是PCR产物分析所用加样器不能拿到其它两个区。

(8) 重复实验，验证结果，慎下结论。

注：本文内容来源于网络，仅供自己学习参考之用。



觉得内容不错，请点赞、评论或分享给需要的朋友！

[如果你热爱生物信息学，欢迎关注我的知乎](https://www.zhihu.com/people/jianzuoyi)，或公众号：简说基因

博客地址：[https://jianzuoyi.github.io/](https://link.zhihu.com/?target=https%3A//jianzuoyi.github.io/)，在这里从零开始学习生信

---

**PCR技术系列文章更新计划：**

[从零开始学PCR技术（零）：PCR技术科普](https://zhuanlan.zhihu.com/p/319757338)

[从零开始学PCR技术（一）：PCR技术简介](https://zhuanlan.zhihu.com/p/315451374)

[从零开始学PCR技术（二）：Taq DNA聚合酶](https://zhuanlan.zhihu.com/p/319408322)

[从零开始学PCR技术（三）：PCR引物设计](https://zhuanlan.zhihu.com/p/322323091)

[从零开始学PCR技术（四）：常见问题](https://zhuanlan.zhihu.com/p/324396902)

从零开始学PCR技术（五）：试验污染

从零开始学PCR技术（六）：多重PCR