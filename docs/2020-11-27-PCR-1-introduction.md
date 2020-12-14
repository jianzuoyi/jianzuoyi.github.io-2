> PCR可能是分子生物学中使用最广泛的技术。虽然我本科学的是生物科学，提过DNA，也跑过PCR，但现在都快忘了PCR的步骤是三个还是四个了。赶快网络搜索之，整理成一个从零开始学系列。

聚合酶链式反应（Polymerase Chain Reaction，PCR）是一项利用DNA双链复制原理，在生物体外复制特定DNA片段的的核酸合成技术。可在短时间内大量扩增目的DNA片段，而不必依赖大肠杆菌或酵母菌等生物体。

DNA的半保留复制是生物进化和传代的重要途径。双链DNA在多种酶的作用下可以变性解旋成单链，在DNA聚合酶的参与下，根据碱基互补配对原则复制成同样的两分子拷贝。在实验中发现，DNA在高温时也可以发生变性解链，当温度降低后又可以复性成为双链。因此，通过温度变化控制DNA的变性和复性，加入设计引物，DNA聚合酶，dNTP就可以完成特定基因的体外复制，这是PCR的理论基础。

## 一、反应体系

PCR反应是在体外模拟DNA的复制过程，因此反应体系中必须具有DNA复制所需的基本要素：

1. 模板（template），含有需要扩增的DNA片段。
2. 引物（primer），一对引物决定了需要扩增的起始和终止位置。
3. 聚合酶（polymerase ），DNA聚合酶复制需要扩增的区域。
4. 脱氧核苷三磷酸（dNTP），用于构造新的互补链。
5. 缓冲液（buffer），提供适合聚合酶行使功能的化学环境。

![](https://jianzuoyi.github.io/img/2020-11-27-pcr.jpg)



## 二、反应步骤

标准PCR过程分为三步：

1. 变性（Denaturation）：利用高温使DNA双链分离。DNA双链之间的氢键在高温下（93 - 98℃）被打断。
2. 退火（Annealing）：在DNA双链分离后，降低温度使得引物可以结合于单链DNA上。
3. 延伸（Extension）：DNA聚合酶由降温时结合上的引物处开始沿着DNA链合成互补链。延伸完成，则完成一轮循环，DNA片段数增加一倍。往复循环这三个步骤25-35次，DNA片段数将得到指数级增加。

![聚合酶链式反应简图](https://jianzuoyi.github.io/img/2020-11-26-PCR-steps.png)

## 三、结果检测

PCR反应扩增出了高的拷贝数，下一步检测就成了关键。荧光素（溴化乙锭，EB）染色凝胶电泳是最常用的检测手段。电泳法检测特异性是不太高的，因此引物两聚体等非特异性的杂交体很容易引起误判。但因为其简捷易行，成为了主流检测方法。近年来以荧光探针为代表的检测方法，有逐渐取代电泳法的趋势。

## 四、技术特点

1. 灵敏度高

   PCR产物的生成量是以指数方式增加的，能将皮克（pg = 10<sup>-12</sup>）量级的起始待测模板扩增到微克（μg=-6）水平。能从100万个细胞中检出一个靶细胞；在病毒的检测中，PCR的灵敏度可达3个RFU（空斑形成单位）；在细菌学中最小检出率为3个细菌。

2. 特异性强

   PCR反应的特异性决定因素：

   * 引物与模板DNA特异正确的结合；
   * 碱基配对原则；
   * Taq聚合酶合成反应的忠实性；
   * 靶基因的特异性与保守性。

3. 简便、快速

   只需要一次性将反应液加好后，就可以进行扩增。一般2~4小时完成扩增反应。扩增产物一般用电泳分析，不一定要用同位素，无放射性污染、易推广。

4. 纯度要求低

   不需要分离病毒或细菌及培养细胞，DNA粗制品及RNA均可作为扩增模板。可直接用临床标本如血液、体腔液、洗漱液、毛发、细胞、活组织等DNA扩增检测。

## 五、发展历史

1971年，Khorana等最早提出核酸体外扩增的设想：经DNA变性，与合适的引物杂交，用DNA聚合酶延伸引物，并不断重复该过程便可合成tRNA基因。但由于当时基因序列分析方法尚未成熟，热稳定DNA聚合酶尚未报道以及引物合成困难，这种想法似乎没有实际意义。

1983年，Kary Mullis首先提出设想。

1985年，Kary Mullis在Cetus公司工作期间，发明了PCR，即简易DNA扩增法。

1985年10月25日申请了PCR的专利，1987年7月28日批准，Mullis是第一发明人。

1985年12月20日在Science杂志上发表了第一篇PCR学术论文，Mullis是共同作者。

1986年5月，Mullis在冷泉港实验室做专题报告，全世界从此开始学习PCR的方法。

1988年，Saiki等将Taq DNA聚合酶用于PCR技术，成功完成了DNA的自动扩增。

1993年10月，Kary Mullis获得了诺贝尔化学奖。

从PCR技术发明至今已过30年，技术迭代已到第三代，在过去的30年里PCR技术为生命科学的发展做出了不可磨灭的贡献。

### 一代PCR

第一代PCR技术就是最初的PCR，采用普通PCR扩增仪来对靶基因进行扩增，然后采用琼脂糖凝胶电泳对产物进行检测，只能做定性分析。

#### 1. 技术应用

能将微量的 DNA 大幅增加。因此对化石中的古生物残骸，犯罪现场的毛发、皮肤碎屑或血液，只要能分离出一丁点的DNA，就能用PCR加以放大，进行比对。

#### 2. 技术优势

灵敏度高，特异性强，简单快捷，对样品的纯度要求低等。

#### 3. 技术缺点

* 最初的PCR技术所采用的核酸染料，会对实验人员和环境造成伤害

* PCR完成之后需要开盖检测，容易发生污染造成假阳性结果

* 检测耗时长，操作麻烦，容易出错

* 只能做定性检测

### 二代PCR

第二代PCR就是荧光定量PCR技术（Real-Time PCR），也叫做qPCR。荧光定量PCR通过在反应体系中加入能够指示反映进程的荧光探针，通过荧光信号的积累来监测扩增产物的积累。通过荧光曲线来判断结果，并可以借助Cq值和标准曲线来定量。

#### 1. 技术应用

用于传染性疾病病原体检测，疾病耐药基因研究，药物疗效考核，遗传疾病诊断。

#### 2. 技术优势

* 污染风险低

* 操作流程更简单、经济高效

* 需要的DNA和RNA加样量少

#### 3. 技术缺点

* 不同厂家生产的试剂和设备所产生的Cq值之间存在一定的差异，并不具备可比性

* 存在背景值的影响，结果易产生偏差

* 对于低拷贝的DNA往往难以检测

* 当反应体系中有PCR抑制物存在时，常规的PCR体系经常会受到影响

### 三代PCR

第三代PCR技术叫做数字PCR（Digital PCR, dPCR, Dig-PCR），这是目前全新的一种PCR检测方式，能对核酸进行检测和定量，采用直接计数目标分子而不依赖任何校准物或者外标，即可确定低至单拷贝的待检靶分子的绝对数目。

#### 1. 技术应用

用于大量正常细胞群中检测少数含突变的细胞。通过稀释样品DNA到对应的检测孔中，经过PCR扩增之后，向每个孔里加入特异性荧光探针与产物杂交，然后直接计数样本中突变型和野生型等位子的数量。

主要应用于突变分析、等位基因缺失、混杂DNA的癌症检测等等。

#### 2. 技术优势

* 灵敏度更高

  数字PCR将传统的PCR反应分割成了数万个体系，这些体系独立扩增，独立检测，保证了个位数的模板数量都可以被检测到。

* 定量更准确

  数字PCR通过微体系的荧光计数，直接将反应初始模板数量统计出来，即使某些微滴中的模板数量不止一个，也可以通过泊松分布进行计算。

* 抗干扰能力更强

  数字PCR第一步反应体系的分配过程中，会将模板和抑制物分配到不同的体系，降低抑制物的干扰。并且，与qPCR不同的是，dPCR检测的是终点荧光，即使微体系稍微受到了影响，也不会影响最终结果的判读。

#### 3. 技术缺点

* 模板质量要求较高

  由于数字PCR将反应拆分成了数万个独立体系，因此其对模板量有比较高的要求，模板量超过微体系量会导致无法定量，过少会导致信号过低，降低定量准确度。

* 非特异性产物的判断

  数字PCR观测的是每个体系中的终点荧光，无论PCR产物是否是特异性产物，只要荧光信号足够强，也是会判读为阳性结果。因此dPCR的引物特异性要求极高。

### PCR各种延伸技术

- [递减PCR](https://www.wanweibaike.com/wiki-遞減PCR)（touchdown PCR）：前几循环温度逐渐下降。
- [逆转录PCR](https://www.wanweibaike.com/wiki-逆轉錄PCR)（RT-PCR）：以由[mRNA](https://www.wanweibaike.com/wiki-MRNA)[逆转录](https://www.wanweibaike.com/wiki-逆转录)而来的cDNA为模板，也因为是从表现型基因来进行增量的，由此产生出来的cDNA产物不带有[内含子](https://www.wanweibaike.com/wiki-内含子)（基因中不具意义的段落），常应用于[分子克隆](https://www.wanweibaike.com/wiki-分子克隆)技术。
- [热启动PCR](https://www.wanweibaike.com/wiki-熱啟動PCR)（hot start PCR）：以高热激活型核酸聚合酶进行反应，减少非专一性产物。
- [即时PCR](https://www.wanweibaike.com/wiki-即時PCR)（real-time PCR）：PCR过程中利用萤光探针或染料定量检测，又称定量PCR（quantitative PCR），可以进行多组对比。
- 巢式PCR（nested PCR）：先用低特异性引物扩增几个循环以增加模板数量，再用高特异性引物扩增。
- [多重PCR](https://www.wanweibaike.com/wiki-多重PCR)（multiplex PCR）：在同一个管中使用多组引物。
- 复原条件PCR（reconditioning PCR）：PCR产物稀释10倍后重新放入原浓度的引物和dNTP等循环3次，以消除产物中的异二聚体。
- dsRNA合成（dsRNA replicator）：合并使用high-fidelity DNA polymersae、[T7RNA聚合酶](https://www.wanweibaike.com/wiki-T7RNA聚合酶)与Phi6 RNA replicase；从双股DNA转录为对应的双股RNA（dsRNA）。可应用于[RNAi](https://www.wanweibaike.com/wiki-RNAi)实验操作。
- [COLD-PCR](https://en.wanweibaike.com/wiki-COLD-PCR) (**co**-amplification at **l**ower **d**enaturation temperature-PCR):用以检测突变或特殊等位基因的PCR应用技术。
- [Digital-PCR](https://en.wanweibaike.com/wiki-Digital_polymerase_chain_reaction)：将标准的PCR反应分割至每一个反应中仅1~2个copy。藉以侦测微小比例的基因差异。应用于：癌症突变基因、病原体检测、借由母血对胎儿做产前检测。

## 六、应用

### 感染性疾病

PCR在医学检验中最有价值的应用领域就是对感染性疾病的诊断。理论上，只要样本中有一个病原体存在，PCR就可以检测到。一般实验室也能检出10~100基因拷贝。PCR对病原体的检测解决了免疫学检测的“窗口期”问题，可判断疾病是否处于隐性或亚临床状态。

### 肿瘤

癌基因的表达增加和突变，在许多肿瘤早期和良性的阶段就可出现。PCR技术不但能有效的检测基因的突变，而且能准确检测癌基因的表达量，可据此进行肿瘤早期诊断、分型、分期和预后判断。

### 遗传病

PCR技术首次临床应用就是从检测镰状细胞和β-地中海贫血的基因突变开始的。基因的突变和缺失均会引起各种珠蛋白的表达不平衡，用FQ-PCR检测各种珠蛋白基因表达差异，是地中海贫血诊断的有效手段。

### 其他

PCR技术还可以应用于生命科学的方方面面，比如：亲子鉴定，分析远古DNA等。

> 一点感想：任何一项技术都不是孤立发展的，需要其他技术的配合。PCR技术也不例外。虽然提出设想很早，但真正变成现实，也是在其他配套技术成熟后才实现的，否则只是空想。

注：本文由网络资料整理而成。



**后续更新计划，敬请期待吧：**

从零开始学PCR技术（一）：PCR技术简介

**从零开始学PCR技术（二）：Taq DNA聚合酶的应用与改造历程**

从零开始学PCR技术（三）：PCR引物设计

从零开始学PCR技术（四）：常见问题

从零开始学PCR技术（五）：试验污染

从零开始学PCR技术（六）：多重PCR的应用