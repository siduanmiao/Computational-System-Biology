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

