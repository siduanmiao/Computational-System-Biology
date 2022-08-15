# Vedio

## Part 1

![image-20220815095732040](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815095732040.png)

![image-20220815104558838](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815104558838.png)

>我们前面已经学过了DNA regulator，但是实际上这个有点不合理，因为当提到基因组的时候人们最先想到的往往是RNA表达（也就是DNA转录成RNA的过程）
>
>hybridization：杂交
>
>微阵列技术是指RNA序列逆转录后，我们将它与汇集了很多基因的芯片探针进行杂交，可以看到不同基因的表达情况。
>
>目前来说用的更多的是RNA-Seq

![image-20220815151246501](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815151246501.png)

>无论我们用了上面哪种方法，我们得到的都是基因的expression level。
>
>每一个列是一个condition下的实验得到的所有基因的表达情况。这个是我们将要讲的，预测gene expression的基础的输入矩阵。

![image-20220815152735585](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815152735585.png)

>然后我们来思考我们可以对这个矩阵做些什么，第一个就是聚类，比如说横向聚类可以说明有一些condition他们的影响是差不多的，纵向聚类说明一些基因的turn on和turn off是相似的。
>
>然后就是分类，我们已知一些基因是属于某些类的，有联系的，这样我们可以依据和他们的相似性，给曾经没有annotation的基因分类。
>
>当然，我们也可以使用这些任务来反过来驱动模型学习对我们expression pattern的latent representation。

![image-20220815154135763](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815154135763.png)



>这一部分是引入的部分，讲的是不要把AI手段当成是唯一的研究手段，PCA，SVD等都是很好的降维手段，还有Autoencoder。

## Part 2

![image-20220815155511996](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815155511996.png)

>首先先来介绍下上采样。
>
>挑战:测量很少的值，推断很多值

![image-20220815155854517](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815155854517.png)

## Part 3

![image-20220815160015448](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815160015448.png)

>Compressed sensing：压缩感知
>
>Compressed sensing (also known as **compressive sensing**, **compressive sampling**, or **sparse sampling**) is a signal processing technique for efficiently acquiring and reconstructing a signal, by finding solutions to underdetermined linear systems。
>
>Composite measure：复合测量
>
>**Composite measure** in statistics and research design refer to composite measures of variables, i.e. measurements based on multiple data items
>
>在这里表达的意思是，我们不是仅仅测量subset of genes，而是使用probe的组合build composite measurement来capture linear combination of gene expression。

## Part 4

![image-20220815194448666](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815194448666.png)

>这里涉及到了TSS和TES：
>
>转录起始位点(Transcription Start Site, TSS)是指一个基因的5’端转录的第一个碱基，它是**转录时，mRNA链第一个核苷酸相对应DNA链上的碱基，通常是一个嘌呤(A或G)**。通常把转录起始点（即5‘末端）前的序列称为**上游(upstream)**，而把其后（即3’末端）的序列称为**下游(downstream)**。启动子（promoter）包含转录点位，这两者是包含与被包含的关系。**启动子是一段DNA片段，一般在转录起始位点的上游**，启动子与与RNA聚合酶结合并能够起始mRNA的合成，启动转录。
>
>左下角这张图，不同颜色的线是不同表达程度的DNA，我们观察基因的甲基化情况。可以看到它们的甲基化水平变化的很大。所以我们甲基化的pattern有可能能够预测gene expression。因为有些样本中RNA降解的非常快，但是我们可以在这些sample中找到甲基化，这样就有预测的潜力。
>
>右边这张图是核小体修饰和gene expression的关系，可以看到，高表达的基因，靠近强enhancer的占比高，而低表达的没有那么多红色区域。所以这个也有可能来预测gene expression level。

## Part 5

这里我们谈预测reporter expression。

![image-20220815200612648](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815200612648.png)

>assay：化验，实验。
>
>因为这个和后面的联系比较大所以学习了下这个技术
>
>首先要了解全基因组关联研究（genome-wide association study, GWAS）：全基因组关联分析(Genome-wide association study)是指在人类全基因组范围内找出存在的序列变异，即单核苷酸多态性(SNP)，从中筛选出与疾病相关的SNPs。
>
>为什么要找到SNP呢?因为人类遗传基因的各种差异，90%可归因于SNP引起的基因变异。
>
>利用GWAS，我们能获得一组信号，这些信号能够告诉我们基因组中的哪些区域与一种特定疾病或性状相关联。但是GWAS的缺点在于，很难找到关键hits，并且GWAS找到的数据一般位于非编码DNA或RNA中。如果想解释基因-变异-环境因素之间的相互作用关系，需要使用GWAS对更多微小的与疾病关联的基因变异进行研究。
>
>而在GWAS基础上利用报告基因，就可以筛选出真正影响基因表达功能的非编码变异。
>
>![image-20220815204741208](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815204741208.png)
>
>![image-20220815204809800](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815204809800.png)
>
>MPRA原理，简单来说就是大规模的GWAS分析。后面会讲GWAS。

然后是splicing

![image-20220815201125686](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815201125686.png)

>**DNA splicing**：DNA拼接是指从一个生物体中移除一部分基因或DNA，并将其补充到另一个生物体中。 DNA是用一种叫做限制性酶的专门化学品来切割的，有成千上万种这样的化学品。 每种限制性酶都有一个独特的、具体的DNA代码，它能够切割出来。
>
>原文：DNA splicing is when a section of genes or DNA, are removed from an organism and supplemented into another.  The DNA is cut using a specialized chemicals called restriction enzymes, there are thousands of these.  Each restriction enzyme has a unique and specific code of, DNA, that it is able to cut out.
>
>但是我们这里说的splicing指的是RNA的splicing
>
>RNA 剪接是分子生物学中的一个过程，其中新制造的前体信使 RNA (pre - mRNA )转录物被转化为成熟的信使 RNA ( mRNA )。它的工作原理是去除所有内含子（RNA 的非编码区）并将外显子（编码区）剪接在一起。对于核编码基因，剪接发生在转录过程中或转录后立即发生在细胞核中。对于那些真核基因如果含有内含子，通常需要剪接来产生可以翻译成蛋白质的 mRNA 分子。对于许多真核生物内含子，剪接发生在一系列由剪接体催化的反应中，剪接体是一种小核核糖核蛋白 ( snRNP ) 的复合体。存在自剪接内含子，即可以催化自身从其亲本RNA分子中切除的核酶。转录、剪接和翻译的过程称为基因表达，是分子生物学的中心法则。
>
>原文：RNA splicing is a process in molecular biology where a newly-made precursor messenger RNA (pre-mRNA) transcript is transformed into a mature messenger RNA (mRNA). It works by removing all the introns (non-coding regions of RNA) and splicing back together exons (coding regions). For nuclear-encoded genes, splicing occurs in the nucleus either during or immediately after transcription. For those eukaryotic genes that contain introns, splicing is usually needed to create an mRNA molecule that can be translated into protein. For many eukaryotic introns, splicing occurs in a series of reactions which are catalyzed by the spliceosome, a complex of small nuclear ribonucleoproteins (snRNPs). There exist self-splicing introns, that is, ribozymes that can catalyze their own excision from their parent RNA molecule. The process of transcription, splicing and translation is called gene expression, the central dogma of molecular biology.
>
>在许多情况下，剪接过程可以通过改变相同 mRNA 的外显子组成来产生一系列独特的蛋白质。这种现象称为[选择性剪接](https://en.wikipedia.org/wiki/Alternative_splicing)。可变剪接可以以多种方式发生。可以延长或跳过外显子，或者保留内含子。据估计，来自多外显子基因的转录本中有 95% 经历了可变剪接，其中一些实例以组织特异性方式和/或特定细胞条件下发生。
>
>原文：In many cases, the splicing process can create a range of unique proteins by varying the exon composition of the same mRNA. This phenomenon is then called alternative splicing. Alternative splicing can occur in many ways. Exons can be extended or skipped, or introns can be retained. It is estimated that 95% of transcripts from multiexon genes undergo alternative splicing, some instances of which occur in a tissue-specific manner and/or under specific cellular conditions。

## Lecture 1

讲的是enhancer的发现。

![image-20220815203417362](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815203417362.png)

>曾经缺少supervised data，我们的方法集中于unsupervised data。现在随着mpra等方法的兴起，我们可以massively probe enhancer然后获取大量的labeled data set。 

![image-20220815205349955](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815205349955.png)

>可以看到，MPRA不是一种具体的方法，这里是MPRA在enhancer识别中的应用。
>
>STARR-seq是一种大规模平行报告分析法，用于直接根据转录增强子在整个基因组中的活性来识别转录增强子，并定量评估增强子活性。
>
>根据上面的流程图所示，我们将不同的fragment插入到想要检测的reporter前面，这样mRNA的表达量就是这个gene所drive的。

后面的模型搭建就不是很理解了。

## Lectue 2

![image-20220815235604034](Lecture%209%20Gene%20Expression,%20Splicing.assets/image-20220815235604034.png)