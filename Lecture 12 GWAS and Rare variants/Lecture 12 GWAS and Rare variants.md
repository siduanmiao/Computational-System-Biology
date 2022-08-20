# Vedio

![image-20220819100101650](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819100101650.png)

>首先我们先了解下什么是disease circuitry.
>
>疾病回路：我的理解是疾病产生的机制。

这节课我们的目的是，我们如何interpret the genetic variation

![image-20220819100716404](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819100716404.png)

>这张图展示的是，给一个病人的基因组，我们找到了几个基因的突变。我们通过执行genome-wide association studys(GWAS)，找到和疾病相关的基因突变，相当于是析因的分析，然后就可以根据这些基因突变来预测疾病。

![image-20220819100644679](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819100644679.png)

## Part 1

注意我们这里只是引入，part 2 还要区分这两个。

![image-20220819105253159](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819105253159.png)

>对于一个染色体上的基因，如果离得够远，那么可以认为是segregare independently, 它们遵循孟德尔定律。但是如果离得很近，它们可以认为是linkage disequilibrium（连锁不平衡）。也就是说它们倾向于co-inherited，也就是一同继承（在染色体的同一位置，上下代之间很明显在继承上有相关性）
>
>LD（linkage disequilibrium）：连锁不平衡
>
>**连锁不平衡（linkage disequilibrium）**是进化生物学与人类遗传学中一个十分重要的概念，因为遗传过程中很多因素能够影响它，而它又会作用于很多因素，包括选择，重组频率，突变率，遗传漂变，交配模式，群体结构等等。反过来看，连锁不平衡就是反应群体遗传过程的一个强有力的信号。
>
>**连锁不平衡**是指 不同**基因座（loci）**的**等位基因（allele）**之间**非随机（nonrandom）的关联**。
>
>首先考虑简单的两基因座情况，设有A, B两个基因座，每个基因做各有两个等位基因，分别用1,2表示。假设每个单倍体型的频率如下所示：
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-424a44b53fffb1e88ae29f2d554e6c60_720w.png)
>
>由上 单倍体型的频率 ，我们也可以简单计算得到各个等位基因的频率：
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-64f260412e724142955006fa17b410bd_720w.png)
>
>如果这两个基因座互相独立不相关（也就是**连锁平衡** **linkage equilibrium** 的状态），那么各个单倍型的频率就可以直接算出，为p1q1 ,p1,q2 , p2q1, p2q2
>
>而实际情况中单倍型的频率对于不相关情况下的理论值会产生偏离（deviation），这个偏离原因即为**连锁不平衡（ linkage disequilibrium ）**，偏离的程度通常记为 **D （连锁不平衡系数，\*coefficient of linkage disequilibrium\*）**
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-5d3b2dcce3fc32dfb3033f3b9be6f162_720w.png)
>
>下图表示了各单倍型频率，各等位基因频率与D之间的关系。
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-2cad6554f881a6311f2d9db828a4ad3a_720w.jpg)
>
>但要注意的是，D值并不是一个用来衡量LD的很好的指标，因为D值会受等位基因频率影响，这使得我们无法比较不同频率的等位基因对之间连锁不平衡的大小。
>
>Lewontin提出通过标准化D值来解决该问题，即用D值除以理论上D可能的最大绝对值：
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-ef2c9982753563e81a72102d12903cac_720w.png)
>
>其中：
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-29c8045985333c26b9c11ab8248a6cc6_720w.png)
>
>但更多的时候我们使用**相关系数（correlation coefficient）r2**来衡量LD：
>
>![img](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/v2-14c03506f4a51df120622463fe330b8b_720w.jpg)
>
>在众多LD的数据库中我们查询到的数值也是基于r2的。
>
>inheritance：遗传
>
>Mendelian Traits：孟德尔性状
>
>repeat length polymorphisms：重复长度多态性
>
>遗传图谱(Genetic linkage map )：又叫连锁图谱（Linkage map）、遗传连锁图谱、染色体图。是指基因或 DNA 分子标记在染色体上的相对位置与遗传距离， 通常以基因或DNA 片段在染色体交换过程中的重组频率厘摩(cM)表示。 1cM 表示两位点在减数分裂中的重组频率为 1％， 重组率的值（cM）值越高表明两位点之间遗传距离越远， 越低表示遗传距离越近。两个基因遗传距离越远，它们之间发生重组事件的概率越高。
>
>传统的QTL定位与GWAS的区别这里有一篇好文章
>
>~~~http
>https://www.plob.org/article/14888.html
>~~~
>
>Quantitative Trait Loci：数量性状基因座
>
>A quantitative trait locus (QTL) is a section of DNA (the locus) which correlates with variation in a phenotype (the quantitative trait).**中文可以翻译成数量性状座位或者数量性状基因座，它指的是控制数量性状的基因在基因组中的位置**
>
>1980s的时候的QTL，也就是传统的QTL，当时已经有了DNA上的一些marker，然后我们可以利用这些maker来定位与性状关联的基因所在的region：
>
>![image-20220819115642387](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819115642387.png)
>
>![QTL 定位的原理](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/1541825730-9968-40b3e29346fe936ea88f03a50338.jpg)
>
>QTL的实质，是确定分子标记与 QTL 之间的连锁关系，也就是连锁分析，基本原理是 QTL 与连锁标记的共分离。
>
>质量性状指相对性状的变异呈不连续性，呈现质的中断性变化的性状。由1对或少数几对主基因控制。
>
>数量性状指相对性状的变异呈连续性，个体之间的差异不明显，很难明确分组。受微效多基因控制，控制数量性状的基因称为数量性状位点(quantitative trait loci, QTLs)。在QTLs中, 基因的效应也有大有小。其中, 效应较大的称为主效QTL, 效应较小的称为微效QTL。
>
>连锁分析（linkage analysis）：是**基于家系**研究的一种方法，它利用连锁的原理研究潜在致病基因与待检测标记基因之间的关系，**来判断待检测标记基因是否一起与潜在致病基因由父代遗传给子代**。
>　　如果同一染色体上的致病基因与待检测基因不连锁，待检测基因将独立于潜在致病基因遗传给下一代，此时待检测标记基因与潜在致病基因位于同一染色体或不同单倍体的几率各一半，否则标明两者之间存在连锁遗传。连锁分析特别适合于单基因疾病的遗传研究，对于复杂疾病的研究具有很大局限性。
>
>关联分析（association analysis）是一种用来分析标记位点的待检测等位基因与疾病易感基因间是否存在关系的分析方法，是在对候选基因进行初步定位或精细定位的基础上，分析候选基因与复杂疾病或数量性状的关系，达到排除不相关基因的目的。
>
>**连锁分析需要在家系中检验等位基因与疾病或者性状间是否为连锁遗传，而关联分析检验群体中疾病或者性状和等位基因间是否存在相关性。**在复杂疾病的分析中，关联分析比连锁分析更为优越。
>
>关联分析的基础是连锁不平衡。常用的方法是基于群体数据的关联分析和基于家庭数据的关联分析及传递不平衡检验。
>
>连锁分析是在家系中计算标记与基因是否连锁，通过重组率计算他们的相对位置，从而确定基因所在的候选区间，但是因为家系的重组次数很少，即便标记非常密集，也很难得到较小的区间。关联分析是检验标记与性状之间是否存在相关性，基于连锁不平衡，确定显著位点周围的区域为候选基因区域，标记越密集，精度越高，甚至直接定位到基因本身，但受到群体结构的影响，这样的显著位点可能存在假阳性。
>
>![image-20220819123627311](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819123627311.png)

![image-20220819142310489](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819142310489.png)

>GWAS不仅可以研究影响大的突变位点，也能研究影响小的突变位点，就像前面的例子，不仅2倍变化能发现，0.1倍的变化也能发现。而传统的方法只能发现影响比较大的variant，对与传统方法来说是unmappable的。
>
>polymorphism：多态性
>
>GWAS是研究的SNP（也就是单核苷酸多态性），研究SNP和疾病的关联。

![image-20220819143954596](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819143954596.png)

![image-20220819144108002](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819144108002.png)

>大多数情况下SNP没有影响，因为它大多数情况下落在非编码区，但是当落入调控区或者蛋白质编码区时会有影响。
>
>这里的alleles不是等位基因的意思，在这个图中是C/G的意思。

![image-20220819144624148](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819144624148.png)

![image-20220819144923058](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819144923058.png)

>这里就是SNP的分类以及一些例子。
>
>注意，这里的minor allele frequency不能理解为最小的等位基因频率，这样会出问题的：
>
>![image-20220819234833152](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819234833152.png)
>
>而我们用MAF来代指这个variant位点的frequency，所以后面我们看到45%这种也不用惊讶。
>
>而Part 2的第一张图，表达的是GWAS适合处理多基因遗传病，而多基因就代表着被多个位点所影响，而位点多了，每个位点的影响就小了，那么疾病在这个位点是选G还是C什么的差别不会很大，这样就前后照应了。

![image-20220819145424039](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819145424039.png)

>所面临的挑战。

## Part 2

![image-20220819145538564](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819145538564.png)

>这个图很形象的体现了关联分析和GWAS的区别，传统的突变位点少，GWAS突变位点多但是每个的作用不强。和前面我们理解的linkage分析，我们发现它在编码区也能跟我们有性状进行联系上，否则不好做关联分析。

![image-20220819145932432](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819145932432.png)

>这张图描述的跟上一张差不多，原因也很简单，如果一个基因的作用非常大，进化不会允许它频率变得很大。
>
>右上角的图的左上角的点离mendacious study就是我们前面描绘的传统方法--linkage analysis。
>
>我们来解读一下右上角这张图，这张图

然后我们详细说明一下linkage analysis

![image-20220819150640829](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819150640829.png)

>这个就是建立基因图谱

![image-20220819150846018](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819150846018.png)

>我们看到，这个下面的数字是marker的个数，说明这个marker和疾病在进化上一起继承的，因为个数都差不多。这个是我个人的理解，实际上也就是研究标记基因的传递和疾病有没有关系，个数都差不多应该是其中一个方面。

![image-20220819152005061](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819152005061.png)

>1. 首先收集大量的个体样本。比如说60000个case和60000个control。当然，很多情况下我们不可能找到那么多的case，所以我们有时候会按照群体患病率来分配case和control。
>
>2. 第二步是genotype它们。这里我们要把genotype方法和测序方法分开：
>
>   genotyping：基因分型
>
>   基因分型和测序是获得核酸信息的两种技术，主要是生物体的DNA 。基因分型和测序之间的主要区别在于，**基因分型是使用标记确定个体拥有哪种遗传变异的过程，而测序是确定给定 DNA 片段中核苷酸序列的正确顺序。**
>
>   基因分型是使用DNA序列和标记以及比较和鉴定其遗传来确定个体的基因组成。基因分型在进化生物学、种群生物学、分类学、生态学和生物体遗传学中很重要。它可以通过不同的技术进行，包括 DNA 测序、聚合酶链式反应、限制性片段长度多态性 (RFLP)、随机扩增多态性检测、扩增片段长度多态性 (AFLP)、DNA 微阵列等。
>
>   基因分型涉及对 DNA 序列的特定小片段进行测序，并使用遗传标记发现遗传组成与其他个体的相关性。它确定个体或特定等位基因之间的单核苷酸多态性（SNP）。基因分型适用于包括人类在内的多种生物。它也适用于微生物，如病毒、真菌等，可用于通过参考谱确定其遗传变异。在分子流行病学和法医微生物学中，通过基因分型获得的信息来控制病原体，尤其是微生物。基因分型在谱系分析中非常重要。对人类进行基因分型以确认母性和父性。基因型将揭示显性和隐性等位基因决定特定性状的基因。
>
>   ![image-20220819155706197](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819155706197.png)
>
>   所以我们这一步没有测序，而是用基因分型的方法去检查了SNP是否存在。
>
>   we are able to catalog common genetic variation,we are able to sequence a bunch of individuals and then systematically catalog what are the common genetic variants in the human population and then go and spot those variants with the G version there and the C version there, and then create probes that hybridize to the G version or the C version depending on whether you carry one, the other, both(i. t two copies of one,two copies of the other or both )
>
>   我们能够对常见的基因变异进行编录，我们对一群个体进行测序，然后系统地对人类群体中常见的基因变异进行编录，然后去发现这些变异G版本在那里，C版本在那里，然后创建与G版本或C版本杂交的探针（至于用一种还是两种，是哪一种，根据我们的纯合子和杂合子来定），这样我们让样本与探针杂交，就知道它其中含有哪些变异了。
>
>3. 然后这一步是质控过程，我们保证样本和我们选用的SNP是合格的。
>4. 4和5都是统计分析方法了，找SNP和疾病的关联，这里就不详细学了，因为这一块的方法实在是太多了。上面的图是QQplot，下面的是卡方检验后的p值做处理后作图。

![image-20220819164954227](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819164954227.png)

>这个是卡方检验同分布的，也就是说，如果这个位点对疾病没有影响，那么疾病组和测试组的A:G应该是相同的，那么我们来检查理论分布和实际分布的区别。

![image-20220819170812760](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819170812760.png)

>因为我们做了很多组的实验，所以我们需要进行P值的校正。

![image-20220819172448366](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819172448366.png)

>作图完成后我们需要进行Fine Mapping (精细映射分析)
>
>fine mapping是GWAS之后的精细分析，通过GWAS分析鉴定出很多variation，但是不清楚哪些是casual variation。通过fine mapping，借助各种统计学模型（如贝叶斯等）来推测出哪些才是真正的casual variation。
>
>因为我们知道，人类自走出非洲进化时间很短暂，也就是说有很多的SNP它们的进化并没有分离开，而是在位点间存在着很多的联系，比如我们看到一个位点是C，我们能够预测它前后的两个位点是G，那么当致病的SNP表达有统计学的差异时，会引起很多不是致病的SNP也产生差异。

![image-20220819195126719](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819195126719.png)

>这是一个很久之前的GWAS实验，为什么点排列成一条线呢？我们可以理解为，染色体很长，和疾病相关的SNPs集中于一小块区域，因为我们把染色体放缩到不足一厘米了，那么这个疾病相关的region显然就好很小了。
>
>第二个问题，为什么有些Linkage可以发现（蓝色），有些不能发现（红色）？这个问题就是下一个图的了

![image-20220819195628399](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819195628399.png)

>我们发现，NOD2位点是Frequency低，effect高（OR值高说明效果显著），是我们前面讨论的linkage能处理的位点类型。

![image-20220819201216355](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819201216355.png)

## Part3

![image-20220819201422515](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819201422515.png)

![image-20220819204244223](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819204244223.png)

>右边这个图，我是按照HiC的理解来的，也就是说，这个纵轴实际上是交互矩阵的对角线。也就是说，我把交互矩阵（方阵）的对角线给画了出来，在这个地方，交互矩阵是所有SNP之间相关性矩阵（里面放的是相关系数，这个相关系数在前面的LD讲了），这个图说明了，SNP之间也是有一个个相互作用比较强的簇的，也就是共进化的簇，簇与簇之间的，和其他的点相关性都不强的，称为recombination hotspot。
>
>Recombination hotspots are **local regions of chromosomes**, on the order of one or two thousand base pairs of DNA (or less—their length is difficult to measure), in which recombination events tend to be concentrated.
>
>单倍体基因型：A haplotype ( haploid genotype) is a **group of alleles in an organism that are inherited together from a single parent**. Many organisms contain genetic material ( DNA) that is obtained from two parents and combined. Normally these organisms have their DNA organized in two sets of pairwise similar chromosomes.
>
>profile有“分析”的意思。

![image-20220819212054541](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819212054541.png)

![image-20220819212109096](Lecture%2012%20GWAS%20and%20Rare%20variants.assets/image-20220819212109096.png)

>介绍LD的，前面资料已经搜集过了。

后面的这部分都是略讲的。

## Part 4

我们现在通过前面的内容已经能够发现association between snps and disease，那么我们想要figure out how it works.

在下一章讲了机制。

## Lecture

这里讲的是他们组内的工作，有点复杂，听不很懂。