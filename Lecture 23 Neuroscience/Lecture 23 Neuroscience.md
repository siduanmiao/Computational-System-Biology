# Lecture 1

![image-20220828150253877](Lecture%2023%20Neuroscience.assets/image-20220828150253877.png)

![image-20220828150645994](Lecture%2023%20Neuroscience.assets/image-20220828150645994.png)

>左边的是科学基础，往往是认知科学家和神经科学家们的发现，提出一些假设。
>
>然后右侧是工程代码这种。
>
>中间就是，利用这些假设搭建神经网络模型，检验假设是否有效。

本节课是一个总结展望类的课，从大的层面讲解人类视觉智能的发展。

![image-20220828151756713](Lecture%2023%20Neuroscience.assets/image-20220828151756713.png)

>当人类观看到这张图片的时候，这张图片只是从屏幕上发出的像素集合（发光强度的集合），我们会提出一些问题（上面的黄色），这些是人类大脑自然而然会产生的问题，这些问题也就是visual intelligence所研究的问题，难易程度由左向右增大

![image-20220828152402544](Lecture%2023%20Neuroscience.assets/image-20220828152402544.png)

>当人类观看一张图像时，人们并不是一次性把一张图片全部看完。人们并不是在视觉的全部区域都有着high acuity（高灵敏度），而是在center of gaze（凝视中心），也就是红点的位置，约10 degree at center of gaze.

![image-20220828153046191](Lecture%2023%20Neuroscience.assets/image-20220828153046191.png)

>那么人是如何inspect the whole scene的？
>
>rapid eye movements,大约200 milliseconds切换一次聚焦的location，sampling the scene as you go。

![image-20220828153343254](Lecture%2023%20Neuroscience.assets/image-20220828153343254.png)

>based on this principle, we can operationalize the problem from all of seeing the understanding of intelligence to a more narrow problem which is more tractable in lab and turn out to be a really good starting point 

![image-20220828154843975](Lecture%2023%20Neuroscience.assets/image-20220828154843975.png)

![image-20220828154902394](Lecture%2023%20Neuroscience.assets/image-20220828154902394.png)

>然后做了视觉实验，观察计算机视觉系统和人类的表现，证明人类仍然是比计算机视觉系统好的，而计算机视觉系统是基于对人类认知科学的假设而构造的神经网络，这说明现有的模型和假设可以趋近实际的人类视觉模型，但是仍有差距。

![image-20220828155620886](Lecture%2023%20Neuroscience.assets/image-20220828155620886.png)

![image-20220828155642808](Lecture%2023%20Neuroscience.assets/image-20220828155642808.png)

>人们又对灵长类动物猴子做了实验，发现他们的表现并不比人的差。

![image-20220828160008880](Lecture%2023%20Neuroscience.assets/image-20220828160008880.png)

>这是目前视觉能力的现状。

![image-20220828164047705](Lecture%2023%20Neuroscience.assets/image-20220828164047705.png)

>因为人的大脑机制非常复杂，我们可以用灵长类动物的研究，其中的inference很有可能在人类大脑中也管用。

![image-20220828232214766](Lecture%2023%20Neuroscience.assets/image-20220828232214766.png)

>视网膜神经节细胞(RGC)是将视觉信息从视网膜传输到大脑的唯一输出神经元。
>
>外侧膝状体（LGN）(Lateral Geniculate Nucleus)是丘脑的一部分，是处理视觉信息的主要中枢。它可以被认为是从视网膜到大脑中整合和响应视觉刺激的主要中继中心，外侧膝状体的视觉投射是连接眼睛和大脑的两条最有力的途径之一。
>
>V1 V2 V4 IT是cortical areas.

![image-20220828233136949](Lecture%2023%20Neuroscience.assets/image-20220828233136949.png)

>当我们的一个图像输入进去后，a pattern of pixels is captured in the back of my eye in this pattern of spiking activity of retinal ganglion cells(视网膜细胞), we have million of retinal ganglion cells arrayed across the back of my retinal.  and then transmits down your optic nerve through the LGN 以及丘脑（V1 V2 V4），在IT处变成new patterns of neural activity.
>
>这里的示意图简化了，一方面，每一个区的神经元中纯在分级激活的现象，另一方面，V1 V2 V4 IT之间并不是一个严格的feed forward chain。
>
>信息从输入到IT大概需要100 millisecond。这个和我们前面的凝视中心维持200 millisecond照应上了。也就是说，我们人类每次看的都是图像的一小块，这一小块的传递是按照这个规律来的。

![image-20220829093702115](Lecture%2023%20Neuroscience.assets/image-20220829093702115.png)

>我们通过在猴子或者其他动物进行我们前面提到的实验，然后像图片中这样用电极在单个神经元附近取样电活动，we do this kind of random sampling within an area like IT.
>
>Spike指的是**大脑神经元动作电位**（即锋电位)，它的发放与传递是大脑神经系统实现信息交互和处理的基础。

![image-20220829094812190](Lecture%2023%20Neuroscience.assets/image-20220829094812190.png)

>这个图的每一个Site是一个神经元，然后每一个site的多行是对这个神经元的多次展示这张图片，蓝色的点是神经元动作电位的记录。
>
>我们可以看到，在IT上动作电位的集中高峰期也是在100msec之后。

![image-20220829095400734](Lecture%2023%20Neuroscience.assets/image-20220829095400734.png)

>这里用了一个定量的方式来衡量100-200msec之间的神经冲动rate

![image-20220829095826086](Lecture%2023%20Neuroscience.assets/image-20220829095826086.png)

>我们采集了100-1000个神经元，但是实际上有百万级别的神经元，这一步其实是under sampled，但是仅仅是这些神经元就能学到很多东西。

![image-20220829100214569](Lecture%2023%20Neuroscience.assets/image-20220829100214569.png)

>我们可以对同一个神经元用很多的图片测试，一个图片测试多次（参照前面几张图），这样我们就可以得到这些神经元对每张图片的反应向量，这个可以理解为一个feature

![image-20220829100409078](Lecture%2023%20Neuroscience.assets/image-20220829100409078.png)

>我们的图片多了后就会成这张图像

![image-20220829102747182](Lecture%2023%20Neuroscience.assets/image-20220829102747182.png)

>当我们用linear classifiers , 也就是linear decoder，对每个样本的分类都训练一个decoder，然后用几十几百的小样本（每个object一组样本）来训练他们，然后检验他们在其它该objects的图像上的泛化性。然后将它的结果总结成行为矩阵（右下角），可以看到它和人以及动物的表现差不多。
>
>我们知道，从pixel来训练是很困难的，但是从IT的信号训练，很简单就能达到和人类差不多的表现，这说明IT feature space is like linearly next to the behavioral pattern. 说明all the computational  questions of this task(visual) have been solved by **pixels->IT**
>
>这种IT neural representation是我们的AI真正想学习的。

![image-20220829103730354](Lecture%2023%20Neuroscience.assets/image-20220829103730354.png)

![image-20220829103841118](Lecture%2023%20Neuroscience.assets/image-20220829103841118.png)

>mean IT firing rate(右上角的绿色矩阵的每个点的值)能够解释行为和感知报告（也就是它们线性模拟可以达到类人的感知结果）
>
>所以我们想要知道pixel是如何到达IT的。

![image-20220829105733761](Lecture%2023%20Neuroscience.assets/image-20220829105733761.png)

>围绕着这个问题，神经学家给出了很多的假设。
>
>蓝框内的是模拟的一个神经元的工作。

![image-20220829110351350](Lecture%2023%20Neuroscience.assets/image-20220829110351350.png)

![image-20220829110501017](Lecture%2023%20Neuroscience.assets/image-20220829110501017.png)

>在这些理论下尝试了很多模型但是都失败了

![image-20220829110544096](Lecture%2023%20Neuroscience.assets/image-20220829110544096.png)

>主要的问题在于，模型的参数并没有被脑科学家确定，而神经网络模型又需要大量的参数。

![image-20220829111233919](Lecture%2023%20Neuroscience.assets/image-20220829111233919.png)

>为了解决这个问题，作者提出了一个模型：给神经网络增加了一个task，为了实现这个core object recognition的任务，我们可以设定loss function,使用反向传播算法更新参数，**用增添task的方式学习到神经系统通过别的机制可能学习到的参数**

![image-20220829111608250](Lecture%2023%20Neuroscience.assets/image-20220829111608250.png)

>然后我们可以将建立的model和实际的神经网络进行比对

![image-20220829111830242](Lecture%2023%20Neuroscience.assets/image-20220829111830242.png)

>以IT的比对的方法为例：
>
>我们知道前面IT的信号是可以写成上面绿色图的形式的，而我们model的这一层的神经元也可以计算一个信号，我们从绿色的图中取出一行，然后数值就可以画成折线图，然后用model预测的结果和它比较

![image-20220829112058936](Lecture%2023%20Neuroscience.assets/image-20220829112058936.png)

![image-20220829112109119](Lecture%2023%20Neuroscience.assets/image-20220829112109119.png)

>最终我们发现，这样学习到的结果比不使用task的好了很多很多

![image-20220829113738331](Lecture%2023%20Neuroscience.assets/image-20220829113738331.png)

>因此，回归了本课刚开始的中心思想，engineering和neuroscience之间的合作共进的关系

![image-20220829144910823](Lecture%2023%20Neuroscience.assets/image-20220829144910823.png)

![image-20220829144948892](Lecture%2023%20Neuroscience.assets/image-20220829144948892.png)



>现在AI 取得了很大的进展，但是在很多方面还不完善，不能和人相媲美

![image-20220829145134958](Lecture%2023%20Neuroscience.assets/image-20220829145134958.png)

>第一个是可解释性的问题，由模型来指导可能的科研方向
>
>第二个是科研方向的进展

![image-20220829145250717](Lecture%2023%20Neuroscience.assets/image-20220829145250717.png)

>视觉腹侧系统（ventral system of visual function）亦称“枕一颞通路”。两个功能特化的视觉系统之一。从初级视皮层Vl区，经次级皮层V2区、V3区，到达V4区，实现物体方位、长度、宽度、空间频率和色调等信息的加工。

![image-20220829150132030](Lecture%2023%20Neuroscience.assets/image-20220829150132030.png)

# Lecture 2

![image-20220829152423403](Lecture%2023%20Neuroscience.assets/image-20220829152423403.png)

>this lecture talk about some work thinking about brains as recurrent neural networks