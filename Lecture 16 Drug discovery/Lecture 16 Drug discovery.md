# Lecture

![image-20220822142009387](Lecture%2016%20Drug%20discovery.assets/image-20220822142009387.png)

![image-20220822150619254](Lecture%2016%20Drug%20discovery.assets/image-20220822150619254.png)

>**Chemical space** is a concept in cheminformatics referring to the property space spanned by all possible molecules and chemical compounds adhering to a given set of construction principles and boundary conditions. It contains millions of compounds which are readily accessible and available to researchers. It is a library used in the method of molecular docking
>
>**化学空间**（Chemical Space）是一个假想的“空间”概念，其中放置着**所有可能**存在的分子，任一特定分子在化学空间中都有一个特定的位置，就像一张巨大的地图上画上了所有的城市。**位置越接近的分子，其特征、性质等也应该越接近。**
>
>化学空间是所有可能分子的集合，其中至少包含$10^{60}$个低于500 Da（道尔顿（Dalton，Da，D）相对原子质量的单位）的有机分子，可能用于药物发现。
>
>functional space：是我们希望达到的特征集合，比如毒性低于多少，溶解性怎么样。
>
>我们的目标就是在化学空间中找到有这些合适性质的化合物。
>
>第一种是基于simulation的，使用类似于molecular dynamics、molecular docking这些方法，比如我们模拟分子在力场中的状态和与protein pocket结合的方式，就能知道蛋白质是不是结合这个分子。
>
>第二种我们称为virtual screening，
>
>**Virtual screening (VS)** is a computational technique used in drug discovery to search libraries of small molecules in order to identify those structures which are most likely to bind to a drug target, typically a protein receptor or enzyme
>
>先导化合物的发现过程中，常用的筛选方式有高通量筛选(High throughput screening，HTS)和虚拟筛选(virtual screening，VS)。
>
>虚拟筛选(virtual screening，VS)是指基于药物设计理论，借助计算机的技术和专业应用软件，从大量化合物中挑选出一些有苗头的化合物，进行实验活性评价的一种方法。其目的是从几十个乃至百万个分子中筛选出新的先导化合物。这种药物筛选方式不消耗样品，降低了筛选的成本，还考虑化合物分子药动学性质和毒性，增加筛选的内涵。并且缩短了新药研发周期，降低了直接研发费用。
>
>虚拟筛选不需要做simulation，只是对先导化合物进行处理，直接从chemical structure 预测性质，然后挑选最优的性质的来进入下游任务。
>
>但是第一种和第二种方法都面临着一个问题，我们有$10^{60}$的小分子，这两种方法都不可能将这些分子全部输入进去。我们的图示也可以很明显的看出，在functional space中各个特征（坐标轴）的量均满足药物设计的，当然我们也可以认为这个图是一个函数，我们想要找药物特征最好的位置就算函数值最大的位置。第一种方法把一个分子对应到里面的一个位置，第二种方法是把所有的位置找出来然后把比较好的分子拿出来（**这个地方的箭头反了，应该是从下指向上**）。而第三个de nova的方法，就是从反方向来考虑这个问题，我们由这些需要的特征，能不能去设计分子。

![image-20220822161214178](Lecture%2016%20Drug%20discovery.assets/image-20220822161214178.png)

![image-20220822161323182](Lecture%2016%20Drug%20discovery.assets/image-20220822161323182.png)

>但是虚拟筛选也不是完全的好，一方面，它能覆盖的药物只有现在存在的化合物，另一方面，它受限于现在已知的特征。
>
>**hand-crafted：** 传统手工方法就是人工设计的一步步能够说出理由来的方法。
>**end-to-end：** 即端到端方法，意思是只有输入端和输出端，当中不需要设计和具体算法，就是一个神经网络
>
>虚拟筛选中我们的特征都是人工设立的，比如辉瑞五原则这种。

![image-20220822162026359](Lecture%2016%20Drug%20discovery.assets/image-20220822162026359.png)

>但是我们的深度学习模型习惯于输出数字，而输出结构就显得很有挑战性。

![image-20220822162157490](Lecture%2016%20Drug%20discovery.assets/image-20220822162157490.png)

![image-20220822163933033](Lecture%2016%20Drug%20discovery.assets/image-20220822163933033.png)

![image-20220822190308684](Lecture%2016%20Drug%20discovery.assets/image-20220822190308684.png)

>生成模型进行新药设计
>
>不需要hand-crafted features了

![image-20220822195320248](Lecture%2016%20Drug%20discovery.assets/image-20220822195320248.png)

>这个是理解drug design问题的一个很好的图，将上面的方法二和三纳入同一张图并用图网络encoding和图网络decoding的方式来理解。

![image-20220822200914222](Lecture%2016%20Drug%20discovery.assets/image-20220822200914222.png)

>这就是最简单的深度学习进行抗生素发现的例子。

![image-20220822201156447](Lecture%2016%20Drug%20discovery.assets/image-20220822201156447.png)

>传统的方法中，我们使用的hand-crafted feature。下面那个是哈希表示的特征，我们chop我们的分子成substructure然后把它们放入哈希表作为一个特征，因为这样的种类很多，所以我们的向量很长，我们需要hash map

![image-20220822203254085](Lecture%2016%20Drug%20discovery.assets/image-20220822203254085.png)

>这个是我们PRP的流程，也是传统的药物设计的流程，但是这个流程有个很重要的问题，因为我们并不知道所有的抗生素的pattern，如果我们知道也就不需要预测了，那么，问题来了，因为我们并不知道所有的pattern，那么我们就不可能完整的概况所有的feature，有些特征可能至今人类没有发现。

![image-20220822203532357](Lecture%2016%20Drug%20discovery.assets/image-20220822203532357.png)

>就像我们曾经学过的CNN提取特征，我们用像素表示图片是一种无损的表示，可以无损的恢复。但是如果是这些feature，他们并不能无损的回复，是经过了一次处理后人为选出来的特征。
>
>理解起来就是，我们给定一个分子结构，我们可以唯一对应无数的分子特征，因为自然界中这些都是确定的。但是，我即使给定再多的分子特征的组合，在庞大的化学空间中，都不可能认为是唯一对应着一个结构。有些特征可能很好，有这些特征的都能很类药，但是我们不能保证我们筛选的特征就是这种特征。

![image-20220822204349109](Lecture%2016%20Drug%20discovery.assets/image-20220822204349109.png)

![image-20220822204633623](Lecture%2016%20Drug%20discovery.assets/image-20220822204633623.png)

![image-20220822204753811](Lecture%2016%20Drug%20discovery.assets/image-20220822204753811.png)

> 然后我们可以把图的信息汇总成一个graph feature representation。 

![image-20220822204906101](Lecture%2016%20Drug%20discovery.assets/image-20220822204906101.png)

>可以很明显的看出，GNN中的特征是机器学出来的，是表示学习的一种，而传统的方法特征是固定的。

![image-20220822212213113](Lecture%2016%20Drug%20discovery.assets/image-20220822212213113.png)

>但是只看结构是不行的，还有一些生物方面发附加信息，有可能也是决定因素。再加上GNN是非常吃数据的，如果我们只有结构数据可能不够。

![image-20220822212903948](Lecture%2016%20Drug%20discovery.assets/image-20220822212903948.png)

>比如这个是预测药物联合使用是不是更有效的。

![image-20220822213036956](Lecture%2016%20Drug%20discovery.assets/image-20220822213036956.png)

>然后这个是引入的一些病毒复制的生物知识。

![image-20220822213341615](Lecture%2016%20Drug%20discovery.assets/image-20220822213341615.png)

![image-20220822213657702](Lecture%2016%20Drug%20discovery.assets/image-20220822213657702.png)

>可以理解为，用外界的知识数据，而不仅仅是结构数据，来补充feature。在feature中加入预测这个化合物能不能和这些target结合，下面的矩阵就像是输入矩阵，看哪些化合物能结合COVID的位点，然后来学习新的compound。

![image-20220822214043319](Lecture%2016%20Drug%20discovery.assets/image-20220822214043319.png)

>当然，结构信息也不能丢失。

