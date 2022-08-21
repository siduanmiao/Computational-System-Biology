# Vedio

![image-20220821100435406](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821100435406.png)

>什么是system genetics：
>
>系统遗传学与系统生物学共享一个整体的、全局的视角。系统生物学的典型策略是扰动系统、监控响应、整合数据并制定描述系统的数学模型。系统遗传学是一种特殊类型的系统生物学，其中群体内的遗传变异被用来扰乱系统。最终，系统遗传学的目标是了解包括疾病在内的复杂性状的广泛分子基础，例如遗传结构和中间生理表型。系统遗传学是一种了解复杂特征的方法，包括常见疾病。它检查中间分子表型，例如转录本、蛋白质或代谢物丰度，以将 DNA 变异与感兴趣的特征联系起来。
>
>Systems genetics shares with systems biology a holistic, global perspective. The typical strategy in systems biology is to perturb a system, monitor the responses, integrate the data and formulate mathematical models that describe the system. Systems genetics is a particular type of systems biology, in which genetic variation within a population is used to perturb the system. Ultimately, the goal of systems genetics is to understand the broad molecular underpinnings, such as genetic architecture and intermediate physiological phenotypes, of complex traits, including diseases.
>
>上节课讲的eQTL，就是在genetic variants和trait中找了表达量作为中间分子表型然后将DNA变异与感兴趣的特征联系了起来。系统遗传学就是这个思想，联想系统生物学中的GEM，我们可以理解为，我们对变异建模。

## Part 1

![image-20220821124503814](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821124503814.png)

>这个是矩阵的乘法，因为我们的线性模型其实就是用很多很多的SNPs来预测set of phenotypes，X是很多很多的location across the genome，而$\theta$是它们的系数矩阵。
>
>至于上节课的公式出现的$Y_{ij}$，意思是对每个individual的set of phenotype都预测了。
>
>上面的公式要求所有的个体间IID（独立同分布），这个很难实现。比如说，一个家庭中。下面的K就是表示，how much of the genetic variance that we've measured is shared by every pair of individuals.
>
>这里我们回顾一下线性模型的假定：
>
>![image-20220821131847719](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821131847719.png)
>
>独立性要求**每一个数据点必须来自于不同的总体**，不同类别y的观察值之间相互独立，相关系数为零。如果我们是从一个家系中选取的，那么很明显他们的观察值并不是独立的。
>
>举一个很简单的例子来理解，当变量之间不独立的情况下，线性回归会遇到的问题：我们对每个孩子的成绩都进行了多次测量
>
>![image-20220821141427462](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821141427462.png)
>
>对于整体而言，我们看到数学成绩和科学成绩是正相关，因为学习好的同学，各科往往都不错，但是我们也能发现，对于单个的学生来说，它的这两者是负相关，也就是，精力有限，学数学就会在学科学上时间少了。



![image-20220821125449530](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821125449530.png)

>可以看到，population structure会影响SNPs在样本中的分布，也会影响到y，这样我们的y就受population structure和实际上的联系的影响了。

![image-20220821125538494](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821125538494.png)

>这个地方属于是把截距效应（随机截距）纳入的混合线性模型。
>
>![image-20220821143316265](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821143316265.png)
>
>![image-20220821143403619](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821143403619.png)
>
>为什么是这个写法呢？因为我们的$u_j$是用到j类的每个样本中的，它的长度和y的长度不一样，需要用设计矩阵Z来对应每个样本是属于哪个类的：
>
>![image-20220821143749594](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821143749594.png)
>
>![image-20220821143801845](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821143801845.png)
>
>除了随机截距模型，还有：
>
>![image-20220821143829502](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821143829502.png)
>
>这里的$\beta_{1j}^{'}$是随机变量，$\mu_j$也是随机变量，因为它们要根据输入的值来变，不同的学校不一样，不同的医生不一样，这种意思。
>
>![image-20220821155001710](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821155001710.png)
>
>然后来理解一个概念：
>
>![image-20220821154116788](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821154116788.png)
>
>![image-20220821154207292](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821154207292.png)
>
>比如说这个里面的这个圈出来的就是随机效应，它是没有固定数值的，样本变它也变。随机变量的话我们就可以用均值，标准差这类的来描述它。
>
>![image-20220821144751355](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821144751355.png)
>
>这里给我的感觉和带交叉项的多元回归很像，因为带交叉项的多元回归，也能够实现不同的组的斜率截距都不同。但是有些时候，多元回归面临的问题很大，比如说，什么时候我应该引入交叉项，以及，引入了交叉项的变量能不能覆盖全部的因素。
>
>![image-20220821155453534](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821155453534.png)
>
>比如如果是人的话，我们怎么可能让每个人成为一个变量进入分类中。
>
>![img](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/20160611122057362.jpeg)
>
>
>
>再往后我也就看不懂了，先理解到这里。

![image-20220821160338534](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821160338534.png)



![image-20220821160348671](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821160348671.png)

![image-20220821160901823](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821160901823.png)

![image-20220821160916373](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821160916373.png)

>这一块暂时看不懂，搁置。

## Part 2

![image-20220821161339270](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821161339270.png)

> ![image-20220821161406736](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821161406736.png)
>
> ![image-20220821161504470](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821161504470.png)

## Part 3

![image-20220821161559963](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821161559963.png)

>heritability是群体遗传学中的概念，意思是表型上的差异（phenotypic variance）有多少比例能被遗传学差异（genetic vairance）解释。那么广义（broad-sense）和狭义（narrow-sense）的区别在哪里呢？
>广义：
>总的genetic variance 与总的phenotypic variance的比值。
>$H^2 = Vg/Vp$,
>$Vg$: genetic variance; $Vp$: phenotypic variance.
>
>狭义：
>可加性genetic variance与总的phenotypic variance的比值。
>$h^2 = Va/Vp$,
>Va: only additive genetic variance.
>
>遗传方差(Genetic variance)：遗传方差又称表型方差（phenotypic variance），通常结合基因型方差（genotype variance）和环境方差（environmental variance）。遗传方差主要包括三方面：加性遗传方差（Additive genetic variance）、显性遗传方差（Dominance genetic variance）和上位遗传方差（Epistatic genetic variance)
>
>表现型值 = 基因型值 + 环境离差（由环境引起的表现型值变化）
>
>基因型值可划分为
>
>G = A + D + I
>
>加性效应（A） ：基因位点内等位基因和非等位基因的累加效应
>
>显性效应（D） ：指基因位点内等位基因之间的互作效应
>
>上位性效应（I） ：非等位基因之间的相互作用
>
>表现型方差 = 基因型方差 + 环境方差
>
>基因型方差可分为
>
>基因加性方差：等位基因间和非等位基因间的累加作用引起的变异量，也称育种值方差。
>
>显性方差 ：等位基因间相互作用引起的变异量，是产生杂种优势的主要方差组分。
>
>上位性方差 ：非等位基因间的相互作用引起的变异量















>人类群体遗传学研究中，**“遗传结构”（ ‘genetic architecture ）是指 对于某一表型，影响广义表型遗传力（ broad-sense phenotypic heritability ）的遗传变异的总和特征**，这是一个整体上的概念。
>
>具体来说，遗传结构包括了 **1. 影响某一表性的变异的数量(#)，2. 对表性影响效应的大小（Beta / OR），3. 群体中这些变异的频率（MAF），以及 4. 这些变异之间或是与环境的相互作用（上位效应 与 G X E**）。
>
>**遗传结构通常被描述为 单基因的（monogenic）、寡基因的（oligogenic）、多基因的（polygenic）、或是全基因的（omnigenic），表示一个，若干，大量，几乎全部遗传变异都对表型变异性有贡献。**
>
>**估计某一表型的遗传结构：**目前主要的方法包括**GWAS**与**gene-based tests**。
>
>![image-20220821114816107](Lecture%2014%20Electronic%20health%20records%20and%20patient%20data.assets/image-20220821114816107.png)



