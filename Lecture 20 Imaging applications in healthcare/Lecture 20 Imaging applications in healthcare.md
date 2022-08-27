# Video

## Lecture 1

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826091316223.png" alt="image-20220826091316223" style="zoom:50%;" />

>精准医疗即，不仅仅关心诊断出病症，而且，不同的病人，患病的程度可能不一样，用药后的反应也可能不一样，根据患者的这些特定的风险情况，为患者设立量身定制的医疗策略。

![image-20220826091847241](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826091847241.png)

>现在是有一些工作在做这个的，比如这个Oncotype DX就是利用22个gene的表达情况来检验risk score，risk score越高，patient越需要aggressive treatment。比如说辅助化疗(chemotherapy)。分数低的话就不太需要化疗。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826092416108.png" alt="image-20220826092416108" style="zoom:67%;" />

>但是这种方法存在着局限性，最明显的一点就是肿瘤的异质性（intra-tumoral heterogeneity），是肿瘤异质性(**Tumour heterogeneity**)的一种。
>
>肿瘤异质性描述了观察到不同的肿瘤细胞可以表现出不同的形态和表型特征，包括细胞形态、基因表达、代谢、运动性、增殖和转移潜能。这种现象既发生在肿瘤之间（**肿瘤间异质性**），也发生在肿瘤内部（**肿瘤内异质性**）。最低水平的肿瘤内异质性是DNA 复制不完善的一个简单结果：每当一个细胞（正常或癌变）分裂时，都会获得一些突变导致癌细胞群多样化。癌细胞的异质性为设计有效的治疗策略带来了重大挑战。然而，对理解和表征异质性的研究可以更好地理解疾病的原因和进展。反过来，这有可能指导创建更精细的治疗策略，这些策略结合了异质性知识以产生更高的疗效。
>
>Tumour heterogeneity describes the observation that different tumour cells can show distinct morphological and phenotypic profiles, including cellular morphology, gene expression, metabolism, motility, proliferation, and metastatic potential.This phenomenon occurs both between tumours (**inter-tumour heterogeneity**) and within tumours (**intra-tumour heterogeneity**). A minimal level of intra-tumour heterogeneity is a simple consequence of the imperfection of DNA replication: whenever a cell (normal or cancerous) divides, a few mutations are acquired—leading to a diverse population of cancer cells.The heterogeneity of cancer cells introduces significant challenges in designing effective treatment strategies. However, research into understanding and characterizing heterogeneity can allow for a better understanding of the causes and progression of disease. In turn, this has the potential to guide the creation of more refined treatment strategies that incorporate knowledge of heterogeneity to yield higher efficacy.
>
>对于恶性的肿瘤细胞，它们更倾向于异构，在一个集团中就会有multiple subclones, multiple different types of mutations。如果我们在采样的时候没有选择到最aggressive component of the tumor。得到的risk score就不能够反映实际的肿瘤情况。

![image-20220826095746085](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826095746085.png)

>这种通过图片分析病情的技术不需要像前面的一样破坏组织，而是模拟了病理学家观察医学影像的操作。

![image-20220826100440833](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826100440833.png)

>这份工作就是，输入进去一个patch，判断有没有细胞核。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826101339011.png" alt="image-20220826101339011" style="zoom:67%;" />

>使用CNN的方法来预测是否heart failure
>
>但是，类似的方法要求模型有重复性，比如说中途使用的一个软件upgrade了，导致产生的图片前后有偏差，那么最终的ACC会下降的非常厉害，因为我们把曾经在那种类型图片上学到的特征，用在了这种图片上。

![image-20220826103349153](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826103349153.png)

![image-20220826103400211](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826103400211.png)

>但是我们不能完全相信AI的这种暴力算法，因为有些情况下它学习到的特征不是我们需要的特征，而是巧合情况下的噪音。

## Lecture 2

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826110455793.png" alt="image-20220826110455793" style="zoom:50%;" />

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826144031377.png" alt="image-20220826144031377" style="zoom:50%;" />

>在lung中，TB有很多的population，它们处在不同的微环境中，这些微环境会改变药物的response，我们要治疗TB，实际上就是要治疗不同的population，所以我们需要很多种类的药物。

![image-20220826144805451](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826144805451.png)

>This is a typical process for drug development and development of multi-drug therapies
>
>我们所忽略的multi-drug是一个很大的空间，比如说有20种药物对TB有效，我们仅仅是两两组合就有190种组合。
>
>现有的研究发现，即便是没有新的药物，新的药物组合在近两年中也能够有很棒的效果。
>
>发现新抗生素的进程非常缓慢，但是TB 领域已经产生了很多新的抗生素，但是组合空间过大而无法测量。

![image-20220826150039863](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826150039863.png)

>他们工作的内容，包括两个方面：
>
>1. narrow in on the single drug space by rapidly using imaging to identify pathway of action of new drugs 
>2. ways that they make systematic combination measurements in vitro and use machine learning to develop classifiers to predict which novel combinations are more likely to be an improvement over the standard of care.

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826162429704.png" alt="image-20220826162429704" style="zoom:50%;" />

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826163140300.png" alt="image-20220826163140300" style="zoom:50%;" />

>不同的药物会引起细胞形态的不同改变。而作用机制相似的药物会使得细胞形态产生相似的变化。
>
>所以考虑，因为我们已经有了很多的药物，我们能不能研究使用该药物后的形态变化然后和参考的药物引起的形态变化做比较，选出变化相似的，机理应该也相似。
>
>该研究基于E.coli

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826164045568.png" alt="image-20220826164045568" style="zoom:50%;" />

>但是我们发现很多细胞的染色并不像前人的工作那样容易，并且形态的变化微小且多变。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826164217172.png" alt="image-20220826164217172" style="zoom:67%;" />

>但是仍然使用多种指标进行了测量。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826164414834.png" alt="image-20220826164414834" style="zoom:67%;" />

>基于前面，设计了这个pipeline，对E.coli有效，我们希望对我们研究TB也有效。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220826170220324.png" alt="image-20220826170220324" style="zoom:50%;" />

>可见，对Ecoli，这种方法分的很好，但是对我们研究的M.tuberculosis，效果非常差，相同的药物作用后都不能被分到一个簇里面去。

## Lecture 3

![image-20220827103135565](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827103135565.png)

![image-20220827103346133](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827103346133.png)

>这里是一些可以量化的phenotype

![image-20220827110056158](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827110056158.png)

>左边的是中性化合物处理的，右边的是药物候选。我们利用DNA content（也可以理解为细胞大小）来作为是sick cell 还是 healthy cell的判断标准。
>
>但是有些情况下，找到一个特定的判断标准是很难的，也就是hand-craft features不容易找到

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827110711040.png" alt="image-20220827110711040" style="zoom:67%;" /><img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827110718283.png" alt="image-20220827110718283" style="zoom: 67%;" />

>比如这两张图片，细胞特征并不是很好找。

![image-20220827111112566](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827111112566.png)

>基于图像的表型，来分析我们所做的处理的效果。

![image-20220827111315493](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827111315493.png)

>本讲座讲的两个方面
>
>1. cell segmentation
>
>   在过去的几年中，细胞分割或识别图像中的细胞已成为一种常用的技术，对基于图像的细胞生物学研究至关重要。使用细胞分割，科学家们能够分析相关的生物学特征，例如细胞计数、类型、分裂、形状等。科学家们可以快速评估这些特征如何随时间变化以及对各种条件的反应。
>
>   **Cell segmentation**, or **identifying cells in an image**, has emerged in the past few years as a commonly used technique crucial for image-based cell biology research.
>
>   Using cell segmentation, scientists are able to analyze relevant biological features such as cell count, type, division, shape, etc. Scientists can quickly evaluate how these features change over time and in response to a variety of conditions.
>
>   通常，术语细胞分割用于指代细胞核的分割（核分割），而不是分割包括细胞质在内的整个细胞体（核+细胞质分割）。在后一种方法中，人们可能会专注于 2D 显微镜图像中的全细胞分割，其中细胞质看起来很亮，背景很暗，并且细胞核几乎没有或没有染色。
>
>   Oftentimes, the term cell segmentation has been used to refer to the segmentation of the cell nuclei (nuclear segmentation) as opposed to segmenting the entire cell body including the cytoplasm (nuclear + cytoplasmic segmentation). In the latter method, one might focus on whole-cell segmentation in the 2D microscopy images where the cytoplasm appears bright, the background is dark, and the nucleus has little or no staining.
>
>   细胞分割任务定位图像中的细胞对象边界，并将这些对象边界与图像背景区分开来。被称为逐像素二元分类，一个完全属于每个感兴趣区域的像素的掩码被推断出来。
>
>   The cell segmentation task localizes cell object boundaries in an image and distinguishes these object boundaries from the background of the image. Known as pixel-wise binary classification, a mask with exactly the pixels that belong to each region of interest is inferred.
>
>   基于逐像素分类的分割方法大致可以分为两类：语义分割和实例分割。
>
>   这两者之间的主要区别在于，在语义分割**中，直接执行像素级分类**，而在实例分割方法中，需要**额外的对象检测步骤**来获取图像中所有类的单个实例。实例分割使用户不仅可以从原始图像中分割出感兴趣的区域，还可以对感兴趣的区域进行分类（例如细菌、门、病毒、细胞核等）
>
>   Segmentation methods based on pixel-wise classification can be roughly divided into two categories: semantic segmentation and instance segmentation.
>
>   The main difference between these two is that in semantic segmentation a **pixel-level classification is performed directly**, while in instance segmentation approaches an **additional object detection step is needed** to obtain the individual instances of all classes in an image. Instance segmentation allows users to not only segment the region of interest from the original image but also to classify what that region of interest is (e.g. bacteria, phyla, virus, a nucleus, etc).
>
>   ![image-20220827112121682](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827112121682.png)
>
>   语义分割执行像素级分类，因此我们看到整个图像只生成一个掩码。此外，无法区分每个类的单个实例。
>
>   同时，当应用实例分割时，我们会看到每个位置都有一个单独的掩码，以便可以单独处理椅子的各个实例。
>
>   The semantic segmentation performs a pixel-level classification, so we see that only one mask for the whole image is generated. Furthermore, individual instances of each class cannot be distinguished.
>
>   Meanwhile, when instance segmentation is applied we see an individual mask for each chair so that individual instances of chairs can be processed separately.

![image-20220827112407180](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827112407180.png)

![image-20220827112435618](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827112435618.png)

>cell segmentation identify where single cells are in images.
>
>因为实际中产生的图像种类和数量都是在不断进步的，生物学家和医学家也致力于使得图像能够包含更多的信息，所以图像的细节和精度也在日益增多，这使得我们的细胞分割算法也要与时俱进

![image-20220827143403574](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827143403574.png)

>图片分割是一个有监督的模型

![image-20220827144317806](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827144317806.png)

>然后介绍了一个数据科学碗的竞赛。

![image-20220827145136842](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827145136842.png)

>最左边的模型使用了ensemble的方法，多个模型投票，计算量非常大。

![image-20220827151723109](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827151723109.png)

>现有的cell segmentation的方法
>
>右上角的就是分析nucleus的，而左上角的甚至在分整个细胞。

![image-20220827151805534](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827151805534.png)

![image-20220827152139673](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827152139673.png)

>可以看到，single-cell representation learning的流程
>
>从原始图片出发，进行图像分割，对单个细胞提取特征矩阵，按照treatment方式分组进行以组为单位的分析，然后进行下游的统计分析任务。

![image-20220827152500237](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827152500237.png)

>传统的特征分析是这样的，但是机器学习可以学习到更高级的，难以直观描述的特征。

![image-20220827152748317](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827152748317.png)

>这里要把perturbation 和 permutation区分开来，permutation test是统计中的置换法，来处理统计量难以计算的时候，得到P值的方法。
>
>而这里的意思是，这个实验是有干扰的实验。
>
>MO：morphology
>
>BE：batch effect
>
>CS：compound
>
>PH：phenotype
>
>解释：batch effect批次效应是指的我们取样的时候，样本之间不是独立的。比如这里，我们细胞培养肯定是在一个plate上有若干细胞，然后用一个compound处理。但是，对于不同的plate之间，不同的时间段处理，不同的人用显微镜观察，不同的实验室环境，都会对MO造成影响（我目前还没搞明白为什么会对CS造成影响）。那么，我们本来的目标是，研究CS对PH的影响，也就是疗效，然后我们通过cell的MO作为中介，来判断药效，但是由于批次效应，引入了误差。
>
>这个和cell segmentation最大的区别在于，我们的PH是没有annotation的，这不是一个监督学习的问题，至今我们都无法确定一个药物是不是对疾病有效，没有普遍的真理，这是药物发现的问题。也就是说，我们想要研究细胞形态来推断药物功能，但是我们药物的功能是没有理论值的，我们并不知道药物用上之后应该是多少，所以没法监督学习，而细胞分割的话，我们显微镜观察后知道细胞应该分成什么样子，可以专家划分。

![image-20220827160500852](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827160500852.png)

>**Embedding**：这个概念在深度学习领域最原初的切入点是所谓的**Manifold Hypothesis**（流形假设）。流形假设是指“自然的原始数据是低维的流形嵌入于(embedded in)原始数据所在的高维空间”。那么，深度学习的任务就是把高维原始数据（图像，句子）映射到低维流形，使得高维的原始数据被映射到低维流形之后变得可分，而这个映射就叫嵌入（Embedding）。比如Word Embedding，就是把单词组成的句子映射到一个表征向量。但后来不知咋回事，开始把低维流形的表征向量叫做Embedding
>
>简单来说，embedding就是用一个低维的向量表示一个物体，可以是一个词，或是一个商品，或是一个电影等等。这个embedding向量的性质是能使距离相近的向量对应的物体有相近的含义，比如 Embedding(复仇者联盟)和Embedding(钢铁侠)之间的距离就会很接近，但 Embedding(复仇者联盟)和Embedding(乱世佳人)的距离就会远一些。
>
>除此之外Embedding甚至还具有数学运算的关系，比如Embedding（马德里）-Embedding（西班牙）+Embedding(法国)≈Embedding(巴黎)
>
>左边的就是利用CNN的分类任务，来驱动模型学习latent space的表征。我们的目标是能够利用这些表征来去处理treatment-level的profiling，后面就可以用这些特征去进行数学分析，如差异矩阵。

![image-20220827161024445](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161024445.png)

>比如说我们学到了每一种药物处理后细胞的形态变化（比如前面CNN驱动的方式）
>
>那么，理想的情况下，作用相似的药物，特征之间的距离会比较近，而不相似的药物会比较远，出现上面图中的这种cluster的情况。
>
>这些都需要更多的实验，甚至临床研究来分析。

![image-20220827161356281](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161356281.png)

![image-20220827161559431](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161559431.png)

>这个是研究突变型的细胞核野生型以及对照组之间的差异。

![image-20220827161651765](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161651765.png)

>这也是测量细胞形态的一个应用。

![image-20220827161858136](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161858136.png)

![image-20220827161909712](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827161909712.png)

>这里讲的是校正批次效应，但是这里我就听不太懂了

![image-20220827164118372](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827164118372.png)

>这个是没有校正的训练集（上面），测试集（下面），左边是不同的药物处理后的分离情况，右边是不同批次的分离情况。可以看到，不同批次的样本之间是有明显的分离情况的。

![image-20220827164031565](Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827164031565.png)

>校正后应该是batch不影响结果，也就是说不同的batch之间应该是没有距离的，混合在一起的。

<img src="Lecture%2020%20Imaging%20applications%20in%20healthcare.assets/image-20220827164414765.png" alt="image-20220827164414765" style="zoom:67%;" />

## Lecture 4/5

这里的两篇工作：

> 1. VoxelMorph: A Learning Framework for Deformable Medical Image Registration
>
>    无监督的医学图像配准模型
>
> 2. Automatic Pathology Detection 自动病理检测，并详细介绍了Y-Net和PS-DeVCEM模型

因为深度学习的底子并不是特别好，所以这里就没有听完本节的两篇工作。