# Vedio

![image-20220821184352680](Lecture%2015%20Graph%20analysis.assets/image-20220821184352680.png)

![image-20220821185512300](Lecture%2015%20Graph%20analysis.assets/image-20220821185512300.png)

## Part 1/2

![image-20220821190220940](Lecture%2015%20Graph%20analysis.assets/image-20220821190220940.png)

>这两部分的内容因为我以前学过了，所以就跳过了。

## Part 3

![image-20220821190424952](Lecture%2015%20Graph%20analysis.assets/image-20220821190424952.png)

>这个地方就是说可以进行SVD

## Part 4

![image-20220821190525834](Lecture%2015%20Graph%20analysis.assets/image-20220821190525834.png)

![image-20220821191011703](Lecture%2015%20Graph%20analysis.assets/image-20220821191011703.png)

![image-20220821191115591](Lecture%2015%20Graph%20analysis.assets/image-20220821191115591.png)

![image-20220821191312832](Lecture%2015%20Graph%20analysis.assets/image-20220821191312832.png)

>本质上是因为PCA得到的特征组合比较复杂，我们想要挑选较少的特征的组合，所以加入正则来限制。

## Part 5

![image-20220821191506098](Lecture%2015%20Graph%20analysis.assets/image-20220821191506098.png)

![image-20220821191547373](Lecture%2015%20Graph%20analysis.assets/image-20220821191547373.png)

![image-20220821191638941](Lecture%2015%20Graph%20analysis.assets/image-20220821191638941.png)

>这里涉及到了拉普拉斯矩阵：
>
> 如下图所示，给定一个有n个顶点的图G=(V,E)，其拉普拉斯矩阵被定义为L=D-A，D其中为图的度矩阵，A为图的邻接矩阵。
>
>![img](Lecture%2015%20Graph%20analysis.assets/v2-6d568ed2e63a0647fe7a3943c4ac4626_720w.jpg)
>
>(2) 该图的邻接矩阵A如下所示，邻接矩阵也就是权重矩阵W：
>
>![image-20220821192043747](Lecture%2015%20Graph%20analysis.assets/image-20220821192043747.png)
>
>(3) 把W的每一列元素加起来得到N个数，然后把它们放在对角线上（其它地方都是零），组成一个N×N的对角矩阵，记为度矩阵D，如下所示。
>
>![image-20220821192052200](Lecture%2015%20Graph%20analysis.assets/image-20220821192052200.png)
>
>(4) 则拉普拉斯矩阵L=D-A，即为：
>
>![image-20220821192059315](Lecture%2015%20Graph%20analysis.assets/image-20220821192059315.png)
>
>理解拉普拉斯矩阵：
>
>![image-20220821192411653](Lecture%2015%20Graph%20analysis.assets/image-20220821192411653-16610810549795.png)
>
>![image-20220821192952159](Lecture%2015%20Graph%20analysis.assets/image-20220821192952159.png)
>
>![image-20220821193004010](Lecture%2015%20Graph%20analysis.assets/image-20220821193004010.png)
>
>我们用高数上的公式来理解：
>
>![image-20220821193357680](Lecture%2015%20Graph%20analysis.assets/image-20220821193357680.png)
>
>![image-20220821193417112](Lecture%2015%20Graph%20analysis.assets/image-20220821193417112.png)
>
>![image-20220821195230238](Lecture%2015%20Graph%20analysis.assets/image-20220821195230238.png)
>
>![image-20220821195253539](Lecture%2015%20Graph%20analysis.assets/image-20220821195253539.png)
>
>![image-20220821195631683](Lecture%2015%20Graph%20analysis.assets/image-20220821195631683.png)
>
>这个图是什么意思呢？
>
>![image-20220821195755016](Lecture%2015%20Graph%20analysis.assets/image-20220821195755016.png)
>
>相当于给它离散化了，不再是一个个紧挨的点
>
>![image-20220821195837231](Lecture%2015%20Graph%20analysis.assets/image-20220821195837231.png)
>
>![image-20220821195901886](Lecture%2015%20Graph%20analysis.assets/image-20220821195901886.png)
>
>这样我就能理解信息增益的意思了。
>
>然后看图中的拉普拉斯矩阵：
>
>![img](Lecture%2015%20Graph%20analysis.assets/v2-e9558644f024554cdca119dfcda1fa8b_720w.jpg)
>
>![image-20220821195957349](Lecture%2015%20Graph%20analysis.assets/image-20220821195957349.png)
>
>![img](Lecture%2015%20Graph%20analysis.assets/v2-1bfc2035f4d2a95d0af6ea0288cd8680_720w.jpg)
>
>![image-20220821200044980](Lecture%2015%20Graph%20analysis.assets/image-20220821200044980.png)
>
>![image-20220821200903604](Lecture%2015%20Graph%20analysis.assets/image-20220821200903604.png)
>
>![image-20220821200923213](Lecture%2015%20Graph%20analysis.assets/image-20220821200923213.png)
>
>

## Part 6

