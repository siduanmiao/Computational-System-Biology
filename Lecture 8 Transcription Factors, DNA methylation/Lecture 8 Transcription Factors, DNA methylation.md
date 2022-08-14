# Vedio

![image-20220812200454001](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220812200454001.png)

这一节课接着上一节课的讲，然后上一节课讲了Part 1的前两个部分，这里补上了一点3D结构然后把Part 2和Part 3的内容讲了，Part 4是例子，没有讲，然后又有一个讲座。

首先来回顾下哺乳动物的细胞核：

![image-20220813194015898](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813194015898.png)

>cytoplasm：细胞质
>
>nucleus：细胞核
>
>nucleolus：核仁
>
>外面黑色的背景就是细胞质。

## Part 1

![image-20220813231006000](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813231006000.png)

然后探讨下染色体结构的探测技术

![image-20220813231224342](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813231224342.png)

>crosslink：交联：交联是指**聚合物链之间通过化学反应连接在一起**
>
>chop up：切割
>
>Flat ends：平末端
>
>sticky end：粘性末端
>
>这个过程可以简单的理解为，我有一碗意大利面，我想要知道蓝色面条是在哪里和红色面条接触的，首先固定住三维结构，然后剪开这个部分的面条，将两个面条连接起来，再进行mapping看这两个部分分别属于染色体的哪个位置，这样，我们就知道哪两个位置互作了。所使用的方法和下面的Hi-C很像，名词也比较接近，可以用下面的辅助理解。
>
>我们将最终的序列测序后，就可以知道，在这个部分的两段，分别在DNA上的哪个地方，这样我们就可以知道DNA上哪两个地方在三维结构上是在一起的。

![image-20220814102027734](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814102027734.png)

>这些是由3C拓展而来的技术，在3C可以测试两个基因组位点是否相互作用的情况下，4C实验的目标是找到多个与单一定位点相互作用的位点，5C的设计采用了多路复用引物和下一代测序(NGS)来确定在一个大的、预先确定的基因组区域内的许多相互作用，测定多点与多点的相互作用，高通量染色体构象捕获(Hi-C)是在整个基因组水平上的功能，旨在测序和检测样品中所有可能的三维相互作用。
>
>Hi-C:
>
>![image-20220814102638599](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814102638599.png)
>
>![image-20220813231845279](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813231845279.png)
>
>![image-20220813231922949](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813231922949.png)
>
>![image-20220813231934906](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813231934906.png)v
>
>![image-20220813232031811](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813232031811.png)
>
>![image-20220813232102064](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813232102064.png)
>
>![image-20220813232125025](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220813232125025.png)

![img](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/v2-1251b676b1582556f81f9e5b0530e0b9_720w.jpg)

![image-20220814104002408](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814104002408.png)

>这个图也很好理解，就是在图上的两个位置之间的交互关系，对角线是最高的因为本质上就是同一个位置，而其他地方则说明了contact。
>
>![image-20220814104304677](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814104304677.png)
>
>从这个图中我们能够发现两个特征：
>
>1. 对角线的的区域倾向于interact with each other，所以对角线很粗
>2. 可以看到有一些区域内的交互比其他区域更加多，topologically associated domain（TAD）.
>3. 有种嵌套的层级结构，也就是说越靠近对角线，交互越明显。对角线往外逐级递减。
>4. 在同一列上，我们可以看到，A更倾向于和A的互作，B更倾向于和B的互作，尽管有可能更远。
>
>![image-20220814105359102](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814105359102.png)
>
>cis interaction：在同一个染色体中的互作
>
>trans interaction：在不同染色体中的互作

![image-20220814105810334](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814105810334.png)

>有关上提到的第四点我们来讲解一下：
>
>![image-20220814105911237](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814105911237.png)
>
>基因组的染色体中包括两个部分，一个是靠近边界的inactive part，一个是靠近中心的active part
>
>![image-20220814120853006](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814120853006.png)
>
>![img](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/3mp14d3s6o.jpeg)
>
>![image-20220814120943598](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814120943598.png)

![image-20220814110310639](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814110310639.png)

>这个就是提到的染色体互作block。

然后我们想要解释TADs的成因：

![image-20220814110835114](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814110835114.png)

>TAD的角峰是loop
>
>![image-20220814121404495](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814121404495.png)
>
>如果我们观察这个block的boundary，我们能够发现CTCF regulator，当两个CTCF regulator bingding towards each other,

![image-20220814114921271](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814114921271.png)

> 这个是不同scale下的互作关系，最大的关系是染色体之间的。然后是compartment，TADs，loops
>
> ~~~http
> https://zhuanlan.zhihu.com/p/338839481
> ~~~
>
> 这篇文章三维结构讲的不错。

## Part 2 

在深度学习方法之前，有一些Classical regulatory genomics

![image-20220814120709320](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814120709320.png)

![image-20220814122122290](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814122122290.png)

>给定我们一些co-expressed基因，我们的假设是它们被一个通用的上游regulator co-regulated，这个regulator结合到所有这些基因的上游。一些人已经开发了算法来找这些上游region的共有的motif。
>
>前面的哪些红色就是我们要寻找的motif，也就是说他们的promoter是被同样的方式调控的，promoter有通用的模体。

![image-20220814155645797](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814155645797.png)

>这一页的理解难度比较高
>
>首先我们要理解什么是期望最大值算法，EM 算法，全称 Expectation Maximization Algorithm
>
>EM 算法的核心思想非常简单，分为两步：Expection-Step 和 Maximization-Step。E-Step 主要通过观察数据和现有模型来估计参数，然后用这个估计的参数值来计算似然函数的期望值；而 M-Step 是寻找似然函数最大化时对应的参数。由于算法会保证在每次迭代之后似然函数都会增加，所以函数最终会收敛。它是贪婪算法的一种，会收敛到局部最优解。
>
>![image-20220814161654860](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814161654860.png)
>
>![image-20220814161756172](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814161756172.png)
>
>然后我们来看这个例子：这一步就类似于我们在模体识别中的用PWM来预测模体，我们找到在当前PWM下可能的模体是什么（极大似然估计），然后，我们后面就要用这些motif，根据最大似然概率去更新PWM。
>
>![image-20220814162014827](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814162014827.png)
>
>然后就可以根据前面E-step得到的隐变量的分布来得到两个硬币的在每一轮中的贡献。
>
>![image-20220814163003195](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814163003195.png)
>
>所以，我们的上面的PPT可以理解为，我们使用PWM来在DNA中寻找motif的instance，然后用这些instance来更新motif的一个迭代的过程。

![image-20220814163707408](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814163707408.png)

>这些方法，并没有细讲，作为了解
>
>真正需要使用的时候，希望可以基于该PPT学习方法。

## Part 3

![image-20220814163924084](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814163924084.png)

![image-20220814183420894](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814183420894.png)

>我们平常输入的RGB的图像是三个channel，这里我们可以认为是输入了四个channel。这个使用的是one-hot encoding，每一个channel是一个核苷酸。之所以称它是convolutional neural network是因为一个filter我们用在了DNA序列的所有位置。
>
>整个过程是通过最后的predict task驱动的。
>
>不同于有三颜色通道（R, G, B）像素组成的二维图片，我们将基因组序列视为有四通道（A, C, G, T）组成的一个固定长度的一维序列窗口。因此，DNA蛋白结合位点预测的问题好比于图片的二分类问题。CNN用于基因组学研究的最大优势之一是，它可以探测某一motif是否在指定序列窗口内，这种探测能力非常有利于motif的鉴定，进而有助于结合位点的分类。

![image-20220814193131143](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814193131143.png)

>这就是所谓卷积的过程

![image-20220814193142237](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814193142237.png)

>加上Thresholding的卷积结果。

## Lecture

![image-20220814193606537](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814193606537.png)

>我们已经知道了很多关于gene regulate的知识，比如说启动子终止子，然后loop的activator，这些知识生化已经做出了卓越的贡献。

![image-20220814193741526](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814193741526.png)

>但是当我们看huge region of DNA sequence的时候，我们就处理不了了，我们已经懂了很多的principle，但是我们对DNA这种语言的precise nature of  language还不甚了解。不过，由于类似于one-hot等编码方式以及理论上可行，我们可以使用机器学习的方法，来完成这类对人来说很难完成的工作。

![image-20220814194505738](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814194505738.png)

>早期的表示方法尝试用数值型向量来表示，比如这个就是所谓的K-mer的表示方法，表示成所有k-mer的频数向量输入进机器学习算法中。
>
>但是k-mer很明显不是好的表示方法。

![image-20220814202301813](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814202301813.png)

![image-20220814202852279](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814202852279.png)

>形式和CNN几乎一模一样

![image-20220814204956940](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814204956940.png)

>这是一些模型的效果

![image-20220814205025639](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814205025639.png)

> Basset模型能够比较好的发现已知的motif

![image-20220814205559224](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814205559224.png)

![image-20220814211520389](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/image-20220814211520389.png)

>Receptive **Field**：感受野（Receptive Field）的定义：卷积神经网络每一层输出的特征图（feature map）上的像素点映射回输入图像上的区域大小。通俗点的解释是，特征图上一点，相对于原图的大小，也是卷积神经网络特征所能看到输入图像的区域。
>
>1）若输入图像的尺寸大小是5*5，经过两次3*3的卷积核（其中stride=1,padding=0）后，其感受野大小为5*5，如下图所示：
>
>![img](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/v2-e9bb5036f5be05aa9d592edf1eeb9839_720w.jpg)
>
>（由卷积计算公式：**N=(W-F+2P)/S+1**，得到第一次卷积后的图像大小为3*3，第二次卷积后的图像大小为1*1）
>
>（2）若输入图像的尺寸大小是7*7，经过三次3*3的卷积核（其中stride=1,padding=0）后，其感受野大小为7*7，如下图所示：
>
>![img](Lecture%208%20Transcription%20Factors,%20DNA%20methylation.assets/v2-5e6f36b7e9e229fab341a60827a0b8a6_720w.jpg)
>
>（由卷积计算公式：**N=(W-F+2P)/S+1**，得到第一次卷积后的图像大小为5*5，第二次卷积后的图像大小为3*3，第三次卷积后的图像大小为1*1）
>
>**也就是说，随着卷积核的增多（即网络的加深），感受野会越来越大。**