# Video

## Lecture 1

![image-20220825094848989](Lecture%2017%20Protein%20folding.assets/image-20220825094848989.png)

>这里涉及到了一个概念:geometric deep learning 几何深度学习
>
>**几何深度学习**，从对称性和不变性的角度，尝试对一大类机器学习问题进行统一。
>
>因此，几何深度学习，**指的不是某一个算法**，而是在许多算法中找到一个共同点，进行概况。
>
>深度学习（表征学习）领域的现状让人想起十九世纪的几何学情况：
>
>**一方面**，在过去十年中，深度学习给数据科学带来了一场革命，使许多以前被认为是无法完成的任务成为可能--无论是计算机视觉、语音识别、自然语言翻译，还是下围棋。**另一方面**，现在有各种不同的神经网络架构，用于不同类型的数据，但很少有统一的原则。
>
>因此，很难理解不同方法之间的关系。
>
>找到算法的共性，以此为框架，作为一种思想，启发后人的算法结构设计。
>
>![image-20220825095653921](Lecture%2017%20Protein%20folding.assets/image-20220825095653921.png)
>
>对于传统的深度学习方法，比如深度神经网络（包括CNN, RNN, LSTM等），我们通常是将一些简单的线性模型，加上一个激活函数，并使用一定的拓扑结构将其堆叠起来的方法。以卷积网络为例，其通常定义一个固定大小的卷积核（也叫Filter，过滤器），并与输入数据 X 的局部区域进行对应元素相乘相加的操作。这种方法在传统的NLP以及CV领域中取得了较为出色的结果，尤其是在图像处理中以卷积神经网络为代表的深度神经网络取得了出色的结果。
>
>这些传统的方法得以实现并广泛应用的一个重要原因是，其输入数据一般定义在比较规则的欧式空间上，比如一维的文本数据，二维的图像数据。这一类数据的重要特性是可以定义出明确的网格结构。这里可以用猫图来举例。
>
>![img](Lecture%2017%20Protein%20folding.assets/v2-6b8e1ae7cb5ca2727d64924904be51c7_720w.jpg)
>
>![image-20220825100605401](Lecture%2017%20Protein%20folding.assets/image-20220825100605401.png)
>
>这里的概念性的东西需要补充一些数学知识：
>
>1. 欧式数据与非欧式数据
>
>   随着网络时代的发展，生活中产生的数据量越来越多，但数据大体分为**两类**：**欧几里得数据、非欧几里得数据**。如下图为两类常见的数据：
>
>   ![img](Lecture%2017%20Protein%20folding.assets/v2-19d2b6fba07bec31678bc510d4cd0540_720w.jpg)
>
>   ![image-20220825100837057](Lecture%2017%20Protein%20folding.assets/image-20220825100837057.png)
>
>2. 欧式空间和非欧式空间
>
>   ![image-20220825101727377](Lecture%2017%20Protein%20folding.assets/image-20220825101727377.png)
>
>   首先引用线代课本的欧氏空间的定义，看起来和数据没有很大的关系，所以在这里我粗略的理解为不规则的数据。
>
>同时这里还涉及到一个概念 fingerprints：表征
>
>分子表面（surface）表征描述了与其他生物分子接触的蛋白质的特征。
>
>这里找到了一篇介绍他工作的文章，先了解下背景再听讲座：
>
>首先从一个蛋白结构中，作者将其分子表面进行离散化处理，形成网格，并将几何和化学特征分配给网格中的每个点（顶点）。对于网格每个顶点，提取曲面几何半径为r =9Å或r =12Å的面积作为一个patch。
>
>其次对于patch中的每个顶点，两个几何描述符（形状指数和与距离有关的曲率）和三个化学描述符（亲水指数，连续性静电以及自由电子和质子供体的位置）被计算出用于输入特征。patch内的顶点使用极坐标进行确定。几何特征（形状指数和与距离有关的率）和极坐标隐式描述了蛋白表面的几何结构（例如，蛋白表面凹穴的“深度”）。
>
>然后MaSIF使用极坐标对这些输入特征进行空间定位，使用一个几何深度神经网络进行训练。该神经网络由一个或多个按顺序应用的层组成；该体系结构的一个关键组成部分是几何卷积，它将将经典卷积推广到曲面，并对patch进行操作。在极坐标系中，我们构造了一个高斯核系统，高斯核将平均patch的顶点特征，并生成维数固定的输出，该输出与一组滤波器相关。一组卷积层被应用于极坐标网格层的输出。其学习过程包括最小化局部核参数集，针对特定应用进行数据训练。这个框架为patch创建了描述符，这些patch可以在神经网络结构中进一步处理。
>
>我们可以看到，所谓的surface fingerprints，就是把蛋白质的表面特性给描述了出来。

![image-20220825103207798](Lecture%2017%20Protein%20folding.assets/image-20220825103207798.png)

![image-20220825104624427](Lecture%2017%20Protein%20folding.assets/image-20220825104624427.png)

>蛋白质结构决定了它的分子功能，而分子功能又可以起到生物功能。

![image-20220825145129788](Lecture%2017%20Protein%20folding.assets/image-20220825145129788.png)

>蛋白质分子能起到的功能有很多

![image-20220825145236723](Lecture%2017%20Protein%20folding.assets/image-20220825145236723.png)

>alpha fold 做的事情和他们的工作是不一样的，alpha fold是从序列出发预测结构，而function prediction是从结构出发希望预测functional fingerprints。

![image-20220825150649736](Lecture%2017%20Protein%20folding.assets/image-20220825150649736.png)

>我们这里研究的就是最后一层的，surface fingerprint来预测蛋白质功能。

![image-20220825150922028](Lecture%2017%20Protein%20folding.assets/image-20220825150922028.png)

>不同的序列，不同的结构，但是却有相似的功能，这些相似性只能通过surface level的层面才能解决。比如说我们用序列的话，就是blast然后看序列间的相似性来判断功能的，而为了满足上面的相似性，我们选择了surface来替代sequence。

![image-20220825151404664](Lecture%2017%20Protein%20folding.assets/image-20220825151404664.png)

>surface fingerprint就像是人脸识别识别人的特征是很像的。我们需要捕捉其中的pattern。

![image-20220825151534276](Lecture%2017%20Protein%20folding.assets/image-20220825151534276.png)

>传统的机器学习的对象，是欧式对象。
>
>而几何深度学习的对象是不规则的对象。
>
>**非欧几里得数据**
>
>![img](Lecture%2017%20Protein%20folding.assets/oikppvhcdu.png)
>
>对于非欧几里得数据，两点之间的最短有效路径不是它们之间的欧几里得距离。我们将使用网格对此进行可视化。在下图中，可以看到，通过离散体素，将经典斯坦福兔子表示为网格（非欧几里得）或呈网格状体积（欧几里得）之间的区别。
>
>![img](Lecture%2017%20Protein%20folding.assets/po6lh3h5zx.png)
>
>点A和B之间的欧式距离是它们之间最短直线路径的长度，可视为图像上的蓝线。两点之间的测地距离，则更类似于绿线的长度。测地距离是高维最短路径概念的表示，而图的测地距离通常是节点之间的最短路径。
>
>以非欧几里德的方式解释网格的优点是，测地距离对于在其上执行的任务更有意义。我们这样想：在深层的CNN中，我们依赖于可能彼此相关的相邻像素。为了在图上重现类似的设置，我们需要考虑重新制定「紧密度」。

![image-20220825152128857](Lecture%2017%20Protein%20folding.assets/image-20220825152128857.png)

>GDL所研究的原型数据就是这种图或者surface
>
>它们可以有不同的表示

![image-20220825152649926](Lecture%2017%20Protein%20folding.assets/image-20220825152649926.png)

>这里选用的就是最后一种，把surface剖分成一个个小的patch

后面的太复杂了，实在是听不懂。

## Lecture 2

>这篇讲座是蛋白质领域华人大佬徐金波做的。是和alpha fold的工作类似的，用序列预测蛋白质结构

![image-20220825173927478](Lecture%2017%20Protein%20folding.assets/image-20220825173927478.png)

>曾经Template-based modeling是首选，但是现在，即使是有模板，如果模板不够好的话也会用template-free modeling，因为现在它的准确度已经很高了。

![image-20220825190100272](Lecture%2017%20Protein%20folding.assets/image-20220825190100272.png)

>1. 简单说就是：仅根据蛋白质的氨基酸序列预测其3D结构的应用（实际上仍然要依赖于片段库）。
>2. 关于两个术语：“Ab initio prediction”和“De novo prediction”中文意思都是“从头预测”，严格意义上前者是真正的从头预测，而后者是基于fragments的预测。但在rosetta的“字典”里，二者是同一个protocol——基于fragments的从头预测。前者ab initio意思是from tlIe beginning，指基于第一性原则(6rst principles)而不依靠同源序列、数据库、二级结构等其它信息，仅靠一条蛋白质序列产生三维结构。后者de novo意思是from the new，是一个更宽泛的含义，指不需要PDB中的同源模板而是依靠对其他结构的观察来预测。
>
>然后了解下蒙特卡洛采样，最早的蒙特卡洛方法都是为了求解一些不太好求解的求和或者积分问题：
>
>例如下图是一个经典的用蒙特卡洛求圆周率的问题，用计算机在一个正方形之中随机的生成点，计数有多少点落在1/4圆之中，这些点的数目除以总的点数目即圆的面积，根据圆面积公式即可求得圆周率
>
><img src="Lecture%2017%20Protein%20folding.assets/v2-036fc4752e53c4aecc97f110442b0fe9_720w.jpg" alt="img" style="zoom:67%;" />
>
>我们知道随机变量函数的数学期望如下：
>
>![image-20220825202756672](Lecture%2017%20Protein%20folding.assets/image-20220825202756672.png)
>
>![image-20220825202817953](Lecture%2017%20Protein%20folding.assets/image-20220825202817953.png)
>
>那么我们接下来就可以讨论蒙特卡洛采样：
>
>![image-20220825203035446](Lecture%2017%20Protein%20folding.assets/image-20220825203035446.png)
>
>![image-20220825203048039](Lecture%2017%20Protein%20folding.assets/image-20220825203048039.png)
>
>![image-20220825203602406](Lecture%2017%20Protein%20folding.assets/image-20220825203602406.png)
>
>![image-20220825203655137](Lecture%2017%20Protein%20folding.assets/image-20220825203655137.png)
>
>![image-20220825203945949](Lecture%2017%20Protein%20folding.assets/image-20220825203945949.png)
>
>这个方法二和方法三都很像，只不过方法二使用了再一次抽样来模拟这个权重，方法三直接使用了比例。
>
>回到这张图，给定一个protein sequence，we cut this sequence into some short segments, each segment has 9 or 11 residues,  then we go to PDB to search fragment for each short segment. So the structure of the segment may be similar of these fragments. 然后我们将这些fragment组合成confirmation，计算energy function，保留confirmation with favorable energy.
>
>但是这个需要太多的sampling。
>
>这是一个temporary modeling

![image-20220825225559623](Lecture%2017%20Protein%20folding.assets/image-20220825225559623.png)

>这个是template free的模型
>
>interaction matrix是最重要的，local structure倒是其次

![image-20220825230202908](Lecture%2017%20Protein%20folding.assets/image-20220825230202908.png)

## Lecture 3

![image-20220826000110824](Lecture%2017%20Protein%20folding.assets/image-20220826000110824.png)

>**位置特异权重矩阵**（Position-Specific Scoring Matrix，简称 PSSM）

这里是讲alpha fold2的工作的。