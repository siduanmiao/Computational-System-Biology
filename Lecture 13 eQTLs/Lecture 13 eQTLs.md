Vedio

![image-20220820100908923](Lecture%2013%20eQTLs.assets/image-20220820100908923.png)

## Part 1

在开始这一部分前，先了解什么是富集分析：

>富集分析，本质上是对数据的分布检验，如果分布集中在某个区域，则认为富集。
>
>生物信息学领域的富集分析：在 **背景基因集(N)** 下获得 **一组特定基因集(S)** ，S可能是基因列表，表达图谱，基因芯片等形式。在预先构建好**基因注释数据库**(例如GO,KEGG等)已对背景基因集(N)根据生物功能或过程进行分类的前提下，通过**统计学算法**找出有那些显著区别于背景基因集(N)的类别(**生物组成/功能/过程**)，或者找出这组特定基因集间在生物组成/功能/过程的共性，经过聚类后去除冗余得到基因富集结果的过程，即为富集分析。
>
>一个生物过程通常是由一组基因共同参与，而不是由单个基因独自完成。富集分析的基本前提假设是，如果一个生物学过程在已知的研究中发生异常，则共同发挥功能的基因极可能被选择出来作为一个与这一过程相关的基因集合。富集分析（Gene Set Enrichment Analysis, GSEA）通常是分析一组基因在某个功能节点上是否相比于随机水平过于出现（over-presentation）
>
>1. 常用数据
>
>- 其中，**背景基因集(N)** 常常是一个物种的基因组注释基因总和。
>- 一组**特定基因集(S)** 常常是差异表达基因集(differentially expressed genes, DEGs)。
>- 预先构建好**基因注释数据库**常用GO或KEGG数据库。
>- 常见的**统计学算法**包括ORA,FCS,PT,NT四种
>
>2. 实际应用
>
>通常会使用其他分析的结果作为**特定基因集(S)**，做基因富集分析来查看这些基因集是否主要集中在某些类别，这些类别代表的功能是否与表型或者进化事件有关联。比如：
>
>- 比较转录组分析得到的差异表达基因集；
>- 比较基因组分析中得到的某物种特有的基因集；
>- 基因家族收缩扩张分析得到的基因组中显著扩张/收缩的基因集；
>- 基因组共线性分析中在全基因组复制事件附近的Ks值的基因集等各种分析得到的基因集；
>
>四类富集分析算法：
>
>![img](Lecture%2013%20eQTLs.assets/v2-c829d356e179334edec8dd6b6fd887f3_720w.jpg)
>
>它的统计原理是用超几何分布型来检验一组基因（共表达或差异表达)中某个功能类的显著性，通过离散分布的显著性分析、富集度分析和假阳性分析, 得出与实验目的有显著关联的、低假阳性率的及靶向性的基因功能类别。
>
>富集涉及到两个概念：前景基因和背景基因。前景基因就是你关注的要重点研究的基因集，背景基因就是所有的基因集。比如做两个样本对照组和处理组的转录组测序，前景基因就是对照组vs处理组的差异基因，背景基因就是这两组样本的所有表达基因。再比如，我想知道与整个广东省相比，深圳市的大学生是不是显著更多（“大学生”就相当于深圳市民的其中一个GO term）。那么前景就是深圳市的人口，背景就是广东省的人口，每个个体都会有一个标签（如大学生、中学生、小学生等）。
>
>因为所谓富集，**就是比较某个GO term里的基因在前景基因所占的比例是否显著高于这个GO term里的基因在背景基因所占的比例，然后根据p<0.05，判断是否有显著富集。**
>
>我们在统计里面很清楚的知道，p值和差值是两个不完全相关的概念，p值小不意味着差距大，同样的，差距大的未必显著，所以我们要把这两者都纳入考虑。
>
>富集分析里的P值计算过程如下：
>
>N和M可以理解为背景基因和前景基因。
>
>![img](Lecture%2013%20eQTLs.assets/v2-a3d8bd05343e662ca7e34c1d1d477842_720w.jpg)
>
>N为所有基因中具有pathway/GO term注释的基因数目；n为N中差异表达基因的数目；M为所有基因中注释为某特定pathway/GO term的基因数目；m为注释为某特定pathway/GO term的差异表达基因数目。
>
>通过计算得到的P value会进一步经过多重检验校正，通常应用的是BH方法，得到FDR值。然后以FDR≤0.05为阈值，满足此条件的pathway/GO term定义为在差异表达基因中显著富集的pathway/GO term。
>
>富集结果的展示方法有多种：
>
>**富集气泡图**
>
>高级气泡图可以对数据库富集的通路进行可视化，是富集常用的可视化图形之一，一般我们会挑选显著分析的前20左右的 pathway/term进行展示，这里以GO富集气泡图为例。
>
>![img](Lecture%2013%20eQTLs.assets/v2-5d305616864f1e2c48dd151987c6aaab_720w.jpg)
>
>*X轴：RichFactor，富集因子，是指前景基因集中属于这个term的基因的数量/背景基因集中富集在这个term中所有基因的数量；*
>
>*Y轴：GO term名称；*
>
>*气泡颜色：Q值（也可以用P值绘图），代表富集显著程度，在这个图形当中，颜色越红代表Q值越小，富集程度越高；*
>
>*气泡大小：数量，前景基因集中属于这个term的基因数量。*
>
> **富集柱状图**
>
>柱状图也是对数据库富集的通路进行可视化的一种方式，是富集常用的另外一种可视化图形，一般来说，它同样挑选显著分析的前20左右的 pathway/term进行展示，这里以KEGG富集结果为例。
>
>![img](Lecture%2013%20eQTLs.assets/v2-9840f3af25fd3943972b7eb7c1180457_720w.jpg)
>
>**X轴：**Gene Percent(%)，柱子长短代表前景基因富集在该pathway上数目占所有前景基因的百分比。柱子上的数字为基因数量，和对应的q值
>
>**Y轴：**Pathway名称；
>
>**柱状图颜色：**Q值（也可以用P值绘图），代表富集显著程度，颜色越深代表Q值越小，富集程度越高。



![image-20220820105726192](Lecture%2013%20eQTLs.assets/image-20220820105726192.png)

>所以我们借用富集分析的思想，可以知道，往组织、调控，细胞类型等上面富集，是可以找到疾病相关的这些东西的。

![image-20220820105936370](Lecture%2013%20eQTLs.assets/image-20220820105936370.png)

>基因组医学的希望与挑战
>
>左边这张图描绘的意思是，我们把Manhattan 图的一部分给zoom in，然后下面这张图的上部分是这些SNP在实验组和对照组之间的差异的一种体现，然后下面的图证明他们有一簇一簇的相关性。

![image-20220820152935318](Lecture%2013%20eQTLs.assets/image-20220820152935318.png)

>这个是向细胞种类富集，富集的方法如下：
>
>第一步是把GWAS找到的所有相关的区域保留下来
>
>然后，因为我们的SNP有LD的特性，我们找到的SNP中并不清楚哪个是起作用的，哪个只是相关的，所以我们把置信区间内的region的SNP全部拿来用。
>
>第三步，分析这些SNP和tissue-specific enhancer的overlap
>
>最后，保留显著富集的组织。
>
>在图上我们可以看到，不同颜色的是这些特异性enhancer和我们序列的overlap的位置，然后我们看这里面和疾病相关的SNP是不是富集。

![image-20220820153706995](Lecture%2013%20eQTLs.assets/image-20220820153706995.png)

>对所有的特征和tissue-specific enhancer都做一遍，就能得到上述的图。

![image-20220820154153891](Lecture%2013%20eQTLs.assets/image-20220820154153891.png)

![image-20220820161003401](Lecture%2013%20eQTLs.assets/image-20220820161003401.png)

fine mapping这一块老师是用的自己组内的工作，bayesian fine mapping，但是涉及了太多组内的专业知识，不太容易入门，所以令找了一篇资料做了解：

>我们通过全基因组关联分析（GWAS）找出来与某个疾病关联最大的基因位点集合（SNP或说variant），GWAS分析的思想如下：
>
>![img](Lecture%2013%20eQTLs.assets/fnyzi48xp8.png)
>
>到这里，其实并没有结束，最终找出来的**若干**基因易感位点（我们不妨称为**易感SNP集合**，每一个位点，简单理解为一个SNP吧），是一个集合，里面包含了可能不止一个易感位点。它们都是在统计意义上的显著，是有一定犯错概率的，也没有经过生物学的证实。 本文要说的精细定位，就是要进一步缩减候选的基因易感位点，排除掉一些“假”的位点。精细定位，叫做fine-mapping。
>
>在做fine-mapping之前，有三个前提一定要具备： 
>
>第一，区域中所有的common SNP都已经被genotyped或者imputed。这个前提是为了确保**真正致病的那个SNP**已经包含在这“若干基因易感位点”之中了。 
>
>第二，已经做过严格的quality control。 
>
>第三，大样本，确保提供足够的power。 
>
>满足必备前提之后，我们进行fine-mapping，分成两部分，statistical fine-mapping和functional fine-mapping。本文的重点是statistical fine-mapping，简单介绍一下统计方法在fine-mapping中的应用。
>
>1. statistical fine-mapping
>
>在此步骤中，我们对GWAS中选出来的易感SNP集合进行统计分析，比较、排序其中SNP的重要次序，甚至删除掉一些不重要的SNP，缩小易感SNP集合的范围。大致有三种方法：
>
>**方法1：conditional regression**
>
>![img](Lecture%2013%20eQTLs.assets/1mg3bivjsz.png)
>
>我们在回归模型中，将最显著的那个SNP作为协变量进行控制，看其他SNP对疾病的影响是否还显著。选出P值最显著的几个易感SNP（P值通常要小于10的-8次方，因为要校正，所以视SNP的数量决定），缩小范围，精细定位。
>
>注：染色体、基因、block和SNP这四者大致是什么关系？
>
>如果把SNP看做是一个具体的房子或者建筑物，那么block就是一片小区，基因大概就是一个城市，染色体差不多是一个省了。
>
>这个也好理解，就相当于是析因分析的样子，看新加入的变量是不是显著，也就是系数是不是等于0，如果把一个变量剥离出来其他的变量都不显著了，说明我们剥离出来的变量相当显著。
>
>例子：
>
>paper：`Fine mapping analysis of HLA‑DP/DQ gene clusters on chromosome 6 reveals multiple susceptibility loci for HBV infection`
>
>这篇文献中，作者想要看一下前人发现的，HLA-DP/DQ这两个基因簇与乙型肝炎（HBV）的显著关系，是否可以再具体定位到某个SNP或者block中。
>
>首先，对基因簇进行分析：
>
>HBV = HLA-DP + （HLA-DQ + other covariates）
>
>HBV = HLA-DQ + （HLA-DP + other covariates）
>
>![img](Lecture%2013%20eQTLs.assets/9cprlozdvp.png)
>
>垂直轴代表作为协变量的基因簇，水平轴代表需要detected的基因簇。白色代表显著，灰色代表不显著。
>
>从两个白色区域可以看出，HLA-DP和HLA-DQ都是显著的，因此，作者的第一个结论是：**之前发现的HLA-DP和HLA-DQ两个基因簇对乙型肝炎的显著影响，是相互独立的。**
>
>此外，作者又对HLA-DP上的三个block做了conditional regression：分别固定一个看其他的两个。
>
>![img](Lecture%2013%20eQTLs.assets/38cnc8kl25.png)
>
>block 3位于HLA-DPA1，block 5位于HLA-DPB1，block 4位于HLA-DPA1和HLA-DPB1的overlap 区域。
>
>| block   | location                          |
>| :------ | :-------------------------------- |
>| block 3 | in HLA-DPA1                       |
>| block 4 | in HLA-DPA1/B1 overlapping region |
>| block 5 | in HLA-DPB1                       |
>
>由图可以看出：
>
>以block 3作为covariate，剩下两个都显著
>
>HBV = block 4 + （ block 3 + other covariates） 
>
>HBV = block 5 + （ block 3 + other covariates）
>
>以block 4作为covariate，剩下两个都显著
>
>最后以block 5作为covariate，剩下两个都不显著。
>
>因此，作者的第二个结论：
>
>**HLA-DPB1上的block 5，是该区域中对HBV作用最显著的易感位点。**
>
>**方法2: Bayesian posterior probability**
>
>P值判断的方法有几个缺点，因为每一个P值的计算都受到样本量、MAF（Minor Allele Frequency）等因素的影响，每个研究的样本量不一样，不同研究的P值之间不好直接比较，而Bayesian posterior probability可以很好的回避这些问题。
>
>对某区域上的每个SNP，计算一个pp（posterior probability）。
>
>![img](Lecture%2013%20eQTLs.assets/6vdwocsqz0.png)
>
>选出的易感SNP集合，其所有的pp之和等于99%，也即丢弃掉的SNP，其PP之和为1%
>
>`"Bayesian refinement of association signals for 14 loci in 3 common diseases"`这是一篇相关的文献。
>
>这篇文献就使用该方法对三种疾病进行fine-mapping。感兴趣的可以自己看一下，这里只展示一张图：
>
>![img](Lecture%2013%20eQTLs.assets/q1q0xqbexz.jpeg)
>
>图中黄色和紫色的点点，就是99%的易感SNP集合，它们的PP加起来为99%。其中，黄色的点点，是95%集合，它们加起来为95%。
>
>这里讲的是用后验概率筛选SNP，但是我对右侧的这个Recombination rate比较好奇，这方面知识比较欠缺，所以搜索了一下。
>
>首先我们要了解重组：
>
>同源重组是一对同源DNA序列交换其DNA的某些部分的过程。在真核生物中，减数分裂过程中的基因重组可以产生一组新的遗传信息，这些信息可以从父母传给后代。
>
>![img](Lecture%2013%20eQTLs.assets/recombination_holliday.png)
>
>然后我们来看cM的定义：
>
>In genetics, a centimorgan (abbreviated **cM**) or **map unit (m.u.)** is a unit for measuring **genetic linkage**. It is defined as the distance **between chromosome positions (also termed loci or markers)** for which the expected average number of intervening chromosomal **crossovers**（注意这里是crossover） in a single generation is 0.01. It is often used to infer distance along a chromosome. However, it is not a true physical distance.
>
>
>
>我们打开遗传学的教科书，首先把交换律、重组率，双交换以及重组和交换的区别这些概念捡回来：
>
>![image-20220820171449465](Lecture%2013%20eQTLs.assets/image-20220820171449465.png)
>
>重组值（recombination value）=重组率（recombination **frequency，注意是frequency不是rate！！**）
>
>那么我们来对上面这个图分析：**我们看亲组合和重组合的时候用的是测交**，所以看的其实是AaBb的配子
>
>![image-20220820174103637](Lecture%2013%20eQTLs.assets/image-20220820174103637.png)
>
>而我们基因图谱上的是交换值。
>
>**重组值/率（这个率是frequency）**的定义：是杂合体产生重组型配子的比例，即重组值/率=重组型配子数/总配子数。在实际操作中一般不直接检测配子基因型，我们就采用测交的方法，转化为重组值/率=测交后代中重组型后代数/总后代数来计算。
>
>可以看出，重组值是某一次杂交实验中，通过统计后代数目，进行计算，实际测出来的值。
>
>**交换值/率的定义**：是染色单体上两个基因之间发生交换的平均次数，即两个基因间发生交换的次数（严格来说应该是交换位点数，因为我们研究的对象是染色单体，发生一次单交换相当于2个交换位点，统计为2次，一次双交换就统计为4次）与总配子数（即总染色单体数）的比例。 
>
>这个时候，我们发现所谓的重组率和交换率
>
>![image-20220820174947489](Lecture%2013%20eQTLs.assets/image-20220820174947489.png)
>
>而cM/Mb
>
>![image-20220820180239862](Lecture%2013%20eQTLs.assets/image-20220820180239862.png)
>
>![image-20220820180315638](Lecture%2013%20eQTLs.assets/image-20220820180315638.png)
>
>目前还不懂这个图什么意思，等用到了再查吧。

## Part 2

![image-20220820184856232](Lecture%2013%20eQTLs.assets/image-20220820184856232.png)

>这里的Mediation Analysis需要了解下：
>
>Mediation Analysis：中介分析。
>
>通俗解释，中介效应是指某个（某些）变量在另两个（两组）变量间扮演了中间人的角色，也就是社会上说的掮客。当然，这里的变量可以是测量变量，也可以是测量模型，如下图所示，如果是测量变量，那么该模型就是一个路径分析模型；如果是一个测量模型，那么就是结构方程模型。
>
>![img](Lecture%2013%20eQTLs.assets/14383547-c0266aaa452546bd.png)
>
>如上图所示，在A变量和C变量之间，存在B变量，只要A到B的路径，以及B到C的路径同时都是通畅的（**A对B有显著性影响，同时B对C有显著性影响**），**那么就可以说在A变量和C变量之间存在由B变量引起的中介效应**。当然，根据A变量和C变量之间的直接路径是否通顺，中介效应又细分为**完全中介效应和部分中介效应**。
>
>检验中介效应是否存在，**其实就是检验A到B，B到C的路径是否同时具有有显著性意义**。为了讲解更有效率，我们以最简单的模型为例，进行说明，如下如所示，图中路径上的符号代表路径系数（**回归系数**）。
>
>![img](Lecture%2013%20eQTLs.assets/14383547-52b5e0cddd0ca062.png)
>
>做中介效应检验的方法目前有四种：**逐步回归法**；**系数乘积检验法**；**差异系数检验法**和**Bootstrapping**。严格意义上来说，它们的分析原理都是一致的，检验W2和W3路径是否同时有意义（通畅），**区别在于判断有意义的标准严谨度不同**。
>
>1. 逐步回归法
>
>   分别检验W1，W2，W3和W1-1是否有显著，如果W2和W3同时有意义，那么中介效应存在；如果W1也有意义，那么就是部分中介，否则就是完全中介。部分中介存在的缺陷容易出现假阳性，因为W2的置信度为95%，而W3的置信度也是95%，如果不加以控制，判断A和B之间存在中介效应的置信度将会降低为95%的平方，也就是90.25%，也就意味着这个结论的可靠性降低了。
>
>2. 系数乘积检验法（Sobel检验）
>
>   鉴于逐步回归法的缺陷，很多研究者创造了修正的方法，系数乘积检验法就是其中一种。系数乘积检验法的原理是将W2和W3综合考虑，也就是考虑W2\*W3是否有意义，这样就避免了分别检验W2和W3造成的置信度降低问题。Sobel检验也存在缺陷，那就是要求W2\*W3服从正态分布，但是这一点是很难保证的，即使是W2和W3服从正态分布，W2\*W3也不一定服从正态分布。
>
>3. 差异系数检验法
>
>   差异系数检验法检验的是(W1-W1-1)是否有意义，因为通常情况下，W2\*W3=(W1-W1-1)，因此，乘积系数法和差异系数法的检验效力是基本上相同的，区别在于两者的标准误不同。经过很多研究者的对比，乘积系数法和差异系数法都比逐步回归法的检验结果更为准确。
>
>4. Bootstrapping法
>
>   大多数假设检验用到的标准误都是做无偏估计或有偏估计得来的，也就是说，检验用的标准误都是伪标准误（估计值），要使估计值准确，需要服从很多的假设条件（例如上面说到的正态分布），系数乘积检验法和差异系数检验法的标准误都是如此。
>
>   有些可惜的是，很多数据无法完全满足标准误估计的假设条件，这样Bootstrapping就应运而生了。这种方法是根据标准误的理论概念，将**样本容量很大的样本**当作总体，进行有放回抽样（抽样次数可以自己定），从而得到更为准确的标准误。

**然后讨论eQTL**

> 表达数量性状位点（expression quantitative trait locus, eQTL）是一类能够影响基因表达量的遗传位点（大部分都是单核苷酸多态性，SNP）
>
> 数量性状基因座：控制数量性状的基因在基因组中的位置称数量性状基因座。常利用DNA分子标记技术对这些区域进行定位，与连续变化的数量性状表型有密切关系
>
> 表达数量性状基因座（expression Quantitative Trait Loci,eQTL）是对上述概念的进一步深化，它指的是染色体上一些能特定调控mRNA和蛋白质表达水平的区域，其mRNA/蛋白质的表达水平量与数量性状成比例关系。
>
> eQTL可分为顺式作用eQTL和反式作用eQTL，顺式作用eQTL就是某个基因的eQTL定位到该基因所在的基因组区域，表明可能是该基因本身的差别引起的mRNA水平变化；反式作用eQTL是指某个基因的eQTL定位到其他基因组区域，表明其他基因的差别控制该基因mRNA水平的差异。
>
> 我们如何理解eQTL呢，比如说，身高是一个数量性状，我们说QTL，就是找和身高相关的所有SNP，而eQTL,即能控制数量性状基因（如身高基因）表达水平高低的那些基因的位点。
>
> 比如说我们对于一个基因X，它的eQTL可以找到，也就是调控它的表达量的SNP。而对于一个性状，它的QTL可以找到。

**为什么我们需要eQTL**

>从基因的改变到疾病等现象的出现，中间缺失了重要的一环，那就是基因的表达。也许在测序中，我们可以看到某一个基因上某一个位置的变化（比如说SNP单核苷酸变化），但是这种变化并不一定会影响mRNA的产生或者蛋白的改变。也就有可能不会影响到疾病或其他生物学过程。于是科学家想到了另一个指标——mRNA的序列数据。因为只有被表转译到mRNA上的基因，才可能进一步表达为蛋白。
>
>简单地说, 遗传学研究经常发现一些致病或易感突变, 这些突变怎样导致表型有时候不太直观; 所以用某个基因的差异表达作为过渡: 突变A-->B基因表达变化-->表型;
>
>**沟通基因改变与疾病的桥梁**
>
>![img](Lecture%2013%20eQTLs.assets/2628465-20211118174202649-2036397651.png)

这样我们就跟标题中的`Intermediate molecular phenotypes to disease`联系起来了

>molecular phenotype(分子表型)：可以从不同层次的窗口（window）观察生命的表现，从原子水平、分子水平、细胞水平、个体水平、群体水平、生态水平、甚至宇观水平，都可以对生命进行观察。通常，观察的记录可以叫做表型（phenotype）。
>
>常见的分子表型有：表观遗传标记（epi-marks），mRNA表达，蛋白质表达修饰等。

![image-20220820193906361](Lecture%2013%20eQTLs.assets/image-20220820193906361.png)

>如果是GWAS的话，我们相当于是想要之间从variant到Disease。这个bridge非常的长，有很多很多的genetic variants，每一个对disease的contribute都很小。

![image-20220820194108418](Lecture%2013%20eQTLs.assets/image-20220820194108418.png)

>这样我们就可以说，SNP通过影响了一些东西最终影响disease。

![image-20220820194223717](Lecture%2013%20eQTLs.assets/image-20220820194223717.png)

>但是这样的挑战是什么呢？因为很多的intermediate phenotypes有可能是disease的结果，而不是disease的原因。（比如生病导致免疫细胞增多），或者环境变化既影响了疾病又影响了intermediate phenotypes。
>
>所以我们分析后面的影响很困难，后面的箭头之间存在着循环。
>
>但是从variant到intermediate phenotype的箭头都是单箭头，这说明可以找它们之间的关系

![image-20220820195051694](Lecture%2013%20eQTLs.assets/image-20220820195051694.png)

>这个是甲基化和SNP的关系

![image-20220820200413056](Lecture%2013%20eQTLs.assets/image-20220820200413056.png)

>meQTL：methylene eQTL
>
>MWAS：methylene-wide association study
>
>因为M和D之间不是单向箭头，MWAS得到的只是correlation而不是causality。
>
>AD：老年痴呆，是我们这里做例子的disease。
>
>iMWAS：imputed MWAS
>
>iM：imputed methylation is the genetic component of methylation，iM是我们meQTL找到的M，它们不太可能是D的结果，所以iM和D之间是单向图而不是双向。 
>
>Impute愿意是归罪,归咎,归因,非难,诋毁。
>
>统计遗传学中意为预测、插补，由已知的基因型预测未知的基因型并对缺失的数据进行补缺。

![image-20220821120624573](Lecture%2013%20eQTLs.assets/image-20220821120624573.png)

>这个是eQTL的经典流程，左上角的是测量每个cell的expression的流程，因为我们要研究的是某一个gene的expression作为中间分子表型，所以选了左边哪个matrix的一行
>
>右上角的图，横轴应该是A的含量，分别在0 0.5 1附近，因为一些校正使得不完全都在正好的0 0.5 1.纵轴应该是什么不太清楚，然后下面的genotype其实指的也就是这个AA AG AT这种。

![image-20220821121253646](Lecture%2013%20eQTLs.assets/image-20220821121253646.png)

>这里的PC是principle components for the genotypes of those individuals的意思。其实就是一些可能跟测量基因型有关联的因素，比如country。下面的ePC就是跟测量表达有关联的因素，比如什么时候测量的，谁负责测量的等等。