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

>这个就是PCA处理MNIST的图。

## Part 5

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