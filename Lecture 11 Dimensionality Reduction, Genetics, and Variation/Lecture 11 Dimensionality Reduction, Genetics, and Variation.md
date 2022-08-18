# Vedio

![image-20220816112740058](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816112740058.png)

![image-20220816150815662](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816150815662.png)

## Part 1

![image-20220816151049265](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816151049265.png)

>这一块有点像是统计的基础，零假设是两个基因的表达无关，备择假设是相关。

![image-20220816151201278](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816151201278.png)

![image-20220816151326068](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816151326068.png)

>然后就是统计上significant的检验，

![image-20220816151552193](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816151552193.png)

>这里是用卡方分布的例子来解释，实际上我们的似然函数检验是需要我们知道x（也就是抽样的分布），下面我们就讨论read count data的分布。

![image-20220816153525963](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816153525963.png)

>这张图也好理解，对poission分布来说，均值方差相等，所以很明显其他两个分布的均值方差应该也是有关系的。
>
>负二项分布：
>
>![image-20220816155801601](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816155801601.png)
>
>![image-20220816160049456](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816160049456.png)
>
>![image-20220816160420914](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816160420914.png)

![image-20220816154936501](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816154936501.png)

>这是一个对bulk data set和single cell data set都很好的方法。

![image-20220816160559344](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816160559344.png)

>这个是超几何分布的方法。

![image-20220816161840673](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816161840673.png)

>下面还讲了校正的问题

![image-20220816161952388](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816161952388.png)

![image-20220816162005420](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816162005420.png)

![image-20220816162013124](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816162013124.png)

## Part 2

![image-20220816163958021](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816163958021.png)

>这个是降维的应用。

![image-20220816164619751](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816164619751.png)

>所谓流形（manifold）就是一般的几何对象的总称。比如人，有中国人、美国人等等；流形就包括各种维数的曲线曲面等。和一般的降维分析一样，流形学习把一组在高维空间中的数据在低维空间中重新表示。和以往方法不同的是，在流形学习中有一个假设，就是所处理的数据采样于一个潜在的流形上，或是说对于这组数据存在一个潜在的流形。对于不同的方法，对于流形性质的要求各不相同，这也就产生了在流形假设下的各种不同性质的假设，比如在Laplacian Eigenmaps中要假设这个流形是紧致黎曼流形等。对于描述流形上的点，我们要用坐标，而流形上本身是没有坐标的，所以为了表示流形上的点，必须把流形放入外围空间（ambient space）中，那末流形上的点就可以用外围空间的坐标来表示。比如R^3^中的球面是个2维的曲面，因为球面上只有两个自由度，但是球面上的点一般是用外围R^3^空间中的坐标表示的，所以我们看到的R^3^中球面上的点有3个数来表示的。当然球面还有柱坐标球坐标等表示。对于R^3^中的球面来说，那末流形学习可以粗略的概括为给出R^3中的表示，在保持球面上点某些几何性质的条件下，找出找到一组对应的内蕴坐标（intrinsic coordinate）表示，显然这个表示应该是两维的，因为球面的维数是两维的。这个过程也叫参数化（parameterization）。直观上来说，就是把这个球面尽量好的展开在通过原点的平面上。

## Part 3

There are many ways of learning these manifolds, including linear ways and non-linear ways.

在学习降维之前，我们首先要了解什么是维数灾难，为什么要降维：

![image-20220817211820735](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817211820735.png)

> 采样困难带来的后果就是**过拟合**，高维空间训练形成的分类器，相当于在低维空间的一个复杂的非线性分类器，这种分类器过多的强调了训练集的准确率甚至于对一些错误/异常的数据也进行了学习，而正确的数据却无法覆盖整个特征空间。为此，这样得到的分类器在对新数据进行预测时将会出现错误。这种现象称之为过拟合，同时也是维数灾难的直接体现。

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/20140829195430114)

> 如图，我们在三维空间中训练的模型向二维空间中投影（可以联想SVM的核函数）

![image-20220818100419296](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818100419296.png)

>过拟合导致泛化性变差，也可以从这个分布上来理解，我们的训练样本没有覆盖全分布，在没有覆盖的地方肯定效果差。

>维数灾难包括两个方面，一个是稀疏性使得采样困难，一个是维数高的话，数据和数据之间的距离开始趋向于一个相同的值。

10 维度

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-9dab4af6ced99aeb665cea8b8e406839_720w.png)

50维度



![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-af6c94ece63068125d46030ce2877aa6_720w.png)

100维度

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-dfe6c915f06ef287c515218d04bd8572_720w.png)



500维度

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-ac81a7fe19f66f6d18597212fd9bac3d_720w.png)



1000维度

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-e425f1ca15e9982b4e4250d032b0c3ab_720w.png)



5000维度

![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/v2-bd0850372c1725dc025ebc0fdae95739_720w.png)

![image-20220818100155474](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818100155474.png)

当然，我们也可以进行说明：

![image-20220818101520788](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818101520788.png)

收敛问题用我个人的理解来看：

![image-20220818235322379](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818235322379.png)

## Part 4

There we talk about linear way: **Principal Component Analysis**

![image-20220816165603098](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816165603098.png)

>PCA is basically asking is there a lower dimensional linear projection of the data that allows me to capture the major source of variation in a deterministic and provably optimal way.

![image-20220816165832443](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816165832443.png)

>Cartesian coordinate system：笛卡尔坐标系
>
>X1...等都是变量。

![image-20220816170249177](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816170249177.png)

>project：映射
>
>这就是PCA所做的事情。

![image-20220816193133464](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816193133464.png)

>这里就用到了线性代数的特征向量的知识。
>
>想表达的含义是这个向量v不会因为转化矩阵S的变化而变化。

![image-20220816193248987](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816193248987.png)

>实对称矩阵的性质,属于不同特征值的实特征向量正交。
>
>半正定矩阵的性质。

![image-20220816194431558](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816194431558.png)

>这就是相似对角化。
>
>这个地方我们观察S，如果我们前面得到的列为cell，行为gene的矩阵，是符合这个S的要求的。

![image-20220816194823949](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220816194823949.png)

>总结上面的线代知识。
>
>PCA方法：选取特征值最高的k个特征向量来表示一个矩阵，从而达到降维分析+特征显示的方法，还有图像压缩的K-L变换。再比如很多人脸识别，数据流模式挖掘分析等方面。这k维是全新的正交特征。这k维特征称为主成分，是重新构造出来的k维特征，而不是简单地从n维特征中去除其余n-k维特征。
>
>那么我们来学习PCA
>
>![image-20220817003656529](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817003656529.png)
>
>![image-20220817003831123](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817003831123.png)
>
>而考虑到我们的数据中，每一列是一个细胞，每一行是一个gene，我们当然希望gene间没有相关性，否则相当于多了的gene可以由别的gene表示，就没有意义了，很符合这个要求。
>
>这个协方差矩阵的推导过程就是利用了线性代数的知识，首先进行了去中心化才能得到x
>
>![image-20220817004756507](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817004756507.png)
>
>![image-20220817100609061](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817100609061.png)
>
>也就是说，我希望我的协方差矩阵是对角矩阵，这样就说明我去相关性成功了。我们知道Q是线性变换，也就是说，我把原来x的数据（当然，是把坐标，也就是列），投影到了新的空间后，使得这个空间在某些维度上的变化非常小，这样可以删除这些低变化维度。
>
>
>
>![image-20220817005401945](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817005401945.png)
>
>![image-20220817005601974](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817005601974.png)
>
>然后因为对角矩阵是按特征值的大小从大到小排的，所以我们知道大的特征值说明相关性越强，这样我们需要多少就取前几行就行
>
>![image-20220817010318503](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817010318503.png)
>
>
>
>这个怎么理解呢？我们从主成分的求解方式来理解：
>
>![image-20220817104822082](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817104822082.png)
>
>去中心化的原因：
>
>![image-20220817011846293](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817011846293.png)
>
>![image-20220817112219959](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817112219959.png)
>
>那么我们会思考，如果不去中心化呢，也就是说，如果我们的原始数据不想要让它归零呢？
>
>![image-20220817115023140](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817115023140.png)
>
>然后我们用投影的方法来理解下矩阵的变换起到的效果：
>
>![image-20220817151317290](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817151317290.png)
>
>![image-20220817151238424](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817151238424.png)

SVD：

>![image-20220817161914389](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817161914389.png)
>
>![image-20220817151822748](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817151822748.png)
>
>**这里要注意，我们这里说特征分解只能分解方阵，并不是说PCA只能降维方阵了，因为PCA实际上做的是计算X^T^ X的特征分解。**
>
>到上面这一步，我们已经能够把矩阵A分解成三个矩阵乘积了，那为什么SVD可以用来降维呢？
>
>![image-20220817153139842](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817153139842.png)
>
>![image-20220817154919149](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817154919149.png)
>
>![image-20220817155456224](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817155456224.png)
>
>![image-20220817155032093](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817155032093.png)
>
>而和PCA相似的，我们也可以将那些“蕴含信息多的”保留下来，而舍弃掉信息少的。
>
>![image-20220817162548148](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817162548148.png)
>
>![image-20220817162631833](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817162631833.png)
>
>那么，PCA和SVD的联系是什么呢？
>
>![image-20220817163210935](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817163210935.png)
>
>![image-20220817163325591](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817163325591.png)
>
>PCA中只用到了X*X^T^的特征矩阵。
>
>![image-20220817163847852](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817163847852.png)
>
>这一段的例子是基于行为样本列为特征说的，所以里面的说法和我的例子中的写法是恰恰相反的，但是体现的含义是，SVD能够删减特征也能删减样本，PCA只能做一个。

![image-20220817204414689](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817204414689.png)

>这个就是PCA处理MNIST的图，它不仅保留了很远的距离特征，比如说6和9，因为比较像所以混的比较近。

## Part 5

PCA尝试维持让原高维空间中的distance matters the same，而t-SNE使得近的更近远的更远。

Then we talk about the non-linear way: `t-SNE`

首先我想要先了解下，什么是线性降维，什么是非线性降维。

>我们首先来看上面那个PCA处理MNIST，我们的PCA是找到数据中**方差最大**的方向并选为主方向，并依次选择稍次的主方向，而为什么这个可视化后会使得不同label间有区分度呢？
>
>![image-20220817204724017](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817204724017.png)
>
>如上图二维到一维的PCA所示，主方向是方差最大的方向，而相同label的点在高维空间中，如果是有区分度的话，那么互相之间也应该是组间距离比较远，组内距离比较近，这样降维后才有区分度。
>
>★线性降维技术。侧重让不相似的点在低维表示中分开。
>
>①PCA（Principle Components Analysis，主成分分析）
>
>②MDS（Multiple Dimensional Scaling，多维缩放）等
>
>★非线性降维技术（广义上“非线性降维技术”≈“流形学习”，狭义上后者是前者子集）。这类技术假设高维数据实际上处于一个比所处空间维度低的非线性流形上，因此侧重让相似的近邻点在低维表示中靠近。

![image-20220817215937677](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817215937677.png)

![image-20220817215950833](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220817215950833.png)

SNE：**Stochastic Neighbor Embedding，随机近邻嵌入**



>![image-20220818104929857](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818104929857.png)
>
>![image-20220818105019550](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818105019550.png)
>
>x和y是向量，有时候会用双竖线，来和数的绝对值区分，||X-Y||就是**向量作差之后各分量的平方和的开根号**，也就是模的概念。
>
>![image-20220818144925697](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818144925697.png)
>
>![image-20220818144940892](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818144940892.png)
>
>
>
>同样，设定$q_{i∣i}=0$。
>
>这个公式看起来跟softmax很像，![image-20220818105230527](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818105230527.png)那么我们可以把上面的公式理解为，$||x_i-x_j||$是两个向量之间的欧氏距离，距离越远那么临近的相似度（也就是这里所谓的条件概率）应该是更低的，那么我们取平方加负号后用类似于softmanx的方法将距离转换为条件概率。
>
>![image-20220818110111171](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818110111171.png)
>
>KL散度就是用一个已知的分布Q来拟合未知的分布P，当然，KL散度是不对称的，这里的$q_{j|i}$小说明低维空间中i和j离得较远，所以条件概率低，高维空间中$p_{j|i}$比较大，说明离得近，就是我们用距离较远的两个点来表达距离较近的两个点，产生的大cost.
>
>![image-20220818110758586](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818110758586.png)
>
>![image-20220819013040522](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819013040522.png)
>
>那么接下来就是优化求解的过程：因为我们是想要在低维空间（y）中表示高维空间（x）的数据，所以我们是要针对y的分布进行优化，也就是说，在高维空间中某一个点$x_i$和其他点的相似度概率的分布应该和低维空间中$y_i$和其他点的相似性概率的分布尽可能接近，让损失函数C最小：
>
>![image-20220818153409730](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818153409730.png)
>
>**这里的推导比较复杂，后面作为附录放进去**

t-SNE：**t-Distributed Stochastic Neighbor Embedding** T分布的随机近邻嵌入

>![image-20220818153746763](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818153746763.png)
>
>拥挤问题（Crowding Problem）：在二维映射空间中，能容纳（高维空间中的）中等距离间隔点的空间，不会比能容纳（高维空间中的）相近点的空间大太多。换言之，哪怕高维空间中离得较远的点，在低维空间中留不出这么多空间来映射。于是到最后高维空间中的点，尤其是远距离和中等距离的点，在低维空间中统统被塞在了一起，这就叫做“拥挤问题（Crowding Problem）
>
>![image-20220818163149526](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818163149526.png)
>
>我们如何理解拥挤问题呢？回到我们映射的方法上，利用分布函数来对应到位置上，假设就按照上面m=8向m=2给映射，我们的p是只跟x（也就是distance）相关的，那么当我们用同分布（高斯分布）的时候，可以看到，大量的堆积到了外壳上。
>
>![image-20220818174314203](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818174314203.png)
>
>![image-20220818154916157](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818154916157.png)
>
>所以我们需要改进联合概率分布，这里简单写一下我的理解：
>
>![image-20220818162848369](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818162848369.png)
>
>
>
>![image-20220818154356934](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818154356934.png)
>
>![image-20220818165850276](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818165850276.png)
>
>![image-20220818165937041](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818165937041.png)
>
>这里我们需要弄明白，这里是怎么用到了高斯分布和T分布，首先我们把高斯分布和t分布的公式写上：
>
>高斯分布：
>
>![image-20220818170152753](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818170152753.png)
>
>t分布：
>
>![image-20220818170648337](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818170648337.png)
>
>我们认真观察t分布和高斯分布，以及它对应的我们计算联合分布函数时的式子，我们能够发现，我们实际上就是认为，在高维空间和低维空间中，对任意一个点，其他的样本点和它的欧氏距离都是符合一个分布的（高斯或者T分布），那么其他的样本点就可以认为是从这个分布中取出来了n-1个点，每个点都对应着分布有一个p(x)，也就是分布（高斯或者T分布）函数在这一点的值。
>
>我们可以想象，如果我们想要把高维的样本映射到低维的样本中并且尽可能不改变数据的分布，那么对于这个点，如果其他n-1个点在分布上所处的位置不边，那么可以说是一种维护了原本数据分布的方法。
>
>![image-20220818171909944](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818171909944.png)
>
>但是我们又没有必要算出来p(x)值，属于无意义的计算量，我们可以转化成$p_{i|j}$，这样我们就可以比较对于任何一个j，它的其余n-1个值的分布和它原来取的那些分布是不是一致。
>
>![image-20220818172105722](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818172105722.png)
>
>不过这个时候我们有可能还有疑问，因为我们对$p(x_i)$进行了归一化变成了偏好性，而不是原始的p值了，那么，为什么要这么做？直接让p值前后保持相等不好吗？确实不好，主要的问题就在于，形状相似的两个分布，分布函数可能并不相同，**这也是我们要学习$\sigma$**的原因，如下图所示
>
>![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/3803770-f8b55c09d4605cad.jpg)
>
>这两个分布相似，但是因为密度不同，分布函数差了很多：
>
>![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/3803770-3ed9389a8bd475ce.jpg)
>
>对这些相似性得分（similarity scores）进行缩放（scale），从而使它们加起来1，计算公式与计算结果如下所示：
>
>![img](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/3803770-8e8e585f5716346c.jpg)
>
>所以这一步是为了让我们高维空间和低维空间的正态分布上的数据分布有可比性。
>
>那么到了这一步，就面临着下一个疑问，既然我们要归一化，那么下面这个图如何理解呢，毕竟我们并不是要它们算出来的p相同，而是归一化的数据相同就可以了。
>
>![image-20220818172608134](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818172608134.png)
>
>![image-20220819011213853](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819011213853.png)
>
>这里我不会推导，但是我认为既然文章这么发了，那么这两个分布应该对应的p的分布是一样一样的。
>
>这里为什么不使用距离而是映射到概率分布也知道了，因为如果使用距离，但是对不同的点，可能它的$\sigma$不同，相同距离的几个点可能意味着不同的分布类型
>
>![image-20220819012307809](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819012307809.png)
>
>可见，到O点同样的距离前者是相对较远，后者却离得很近。而且距离保持一致理论上很难做到，比如下面的二维到一维就不可能做到，除非本身就是维数低的“流形”。
>
>![image-20220819012627718](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819012627718.png)
>
>这样我们就可以理解这张图，对于较大相似度的点，t分布在低维空间中的距离需要稍小一点；而对于低相似度的点，t分布在低维空间中的距离需要更远。对于某一概率分布区间（下图的最下面的两条线），我们的数据在高维空间的距离是在红色范围内，而投影到低维后到了黄色的范围，这一块的体积（低维空间的超球壳）更大，这样就大大缓解了拥挤度的问题。而且还起到了一种类似于变换的效果，这恰好满足了我们的需求，即**同一簇内的点(距离较近)聚合的更紧密，不同簇之间的点(距离较远)更加疏远。**因此这种方法映射后聚类的效果会十分明显。
>
>![image-20220818174810403](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818174810403.png)
>
>优化的动态过程如下：
>
>![optimise](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/t-sne_optimise.gif)
>
>SNE保留局部特征中，T分布是理论上让近的更近远的更远，而KL散度则是在优化上，尽可能保留局部特征，而可以放弃一部分较远的特征。
>
>有关SNE的公式推导如下：
>
>~~~http
>https://zhuanlan.zhihu.com/p/384698107
>~~~
>
>推导并不是很难，主要是可以加深下理解以及链式法则的一些内涵，有空的时候推一下。

![image-20220818211018011](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818211018011.png)



>可以看到t-SNE分的更开了。

对于这种高维的图像，我们认为每一个像素点是一个特征：

![image-20220818213123590](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818213123590.png)

![image-20220818213402405](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220818213402405.png)

![image-20220819013124636](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819013124636.png)

![image-20220819013159956](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819013159956.png)

![image-20220819013220952](Lecture%2011%20Dimensionality%20Reduction,%20Genetics,%20and%20Variation.assets/image-20220819013220952.png)

>因为我们只考虑了固定数量的邻居。

