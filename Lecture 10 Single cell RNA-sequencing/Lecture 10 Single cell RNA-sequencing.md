# Vedio

![image-20220816092148715](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816092148715.png)

## Part 1

![image-20220816094018376](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816094018376.png)

>individual cells are different from each other. 
>
>不同种类的细胞之间，同种细胞内部都是存在着差异。

![image-20220816094507755](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816094507755.png)

>如果我们用whole-sample 的分析，均值可能没有代表性，罕见的情况可能会丢失。

![image-20220816100547429](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816100547429.png)

![image-20220816100721391](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816100721391.png)

![image-20220816100919614](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816100919614.png)

>这个就是scRNA-seq，右下角的图是最终的结果，每一列是一个时间的cell的基因表达情况，每一行是一种gene。

![image-20220816102258407](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816102258407.png)

>纵轴是不同的基因，我们能看到，有些gene的表达量，单个gene和大量gene没有什么不同，但是有的区别就很大。

![image-20220816102554213](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816102554213.png)

>FISH：fluorescence in situ hybridization  荧光原位杂交
>
>是以荧光标记取代同位素标记而形成的一种新的原位杂交方法
>
> RNA-FISH原理：如果待检测的细胞或组织切片上的靶核酸与所用的核酸探针是同源互补的，二者经变性-退火-复性，即可形成靶核酸与核酸探针的杂交体。将核酸探针的某一种核苷酸标记上报告分子如生物素或直接标记荧光素，可利用该报告分子与荧光素标记的特异亲和素之间的免疫化学反应或直接经荧光检测体系在镜下对待测核酸(mRNA、lncRNA、circRNA、miRNA)进行定性、半定量或相对定位分析的一种实验方法。
>
>这三个基因分别是：robustly expressed, partially expressed, rarely expressed.
>
>下面的表是它们信号的分布。

![image-20220816103033612](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816103033612.png)

>管家基因表达比较保守，而很多基因表达的变化比较大。

## Part 2

![image-20220816103443822](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816103443822.png)

>scale up：放大，提高

![image-20220816103640472](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816103640472.png)

>单细胞分离方法的拓展。

![image-20220816103941086](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816103941086.png)

>FACS：Fluorescence activated Cell Sorting 流式细胞荧光分选技术

![image-20220816104331325](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816104331325.png)

>![image-20220816111139441](Lecture%2010%20Single%20cell%20RNA-sequencing.assets/image-20220816111139441.png)
>
>左边的是用well而右边的是用droplet，droplet带着bar code，把单细胞分开。颜色就是bar code，我们做的和普通的RNA-seq区别不大，不过用barcode来识别它们识别与哪个cell。这也是一个massively parallel的方法。
>
>中间的方法，不做well也不做droplet。

