![image-20220827183516538](Lecture%2021%20EHRs%20and%20data%20mining.assets/image-20220827183516538.png)

![image-20220827191122936](Lecture%2021%20EHRs%20and%20data%20mining.assets/image-20220827191122936.png)

>目前有大量的医疗数据，我们可以进行data mining，找到其中蕴含的substructure。这里用的是无监督学习的方法。（右上）
>
>构建clinical tools。

![image-20220827191909528](Lecture%2021%20EHRs%20and%20data%20mining.assets/image-20220827191909528.png)

>Disease or patient registries are collections of secondary data related to patients with a specific diagnosis, condition, or procedure, and they play an important role in post marketing surveillance of pharmaceuticals. Registries are different from indexes in that they contain more extensive data
>
>病例注册登记（patient registry）通常是指涉及健康信息的登记。狭义的病例注册登记研究是为了达到一种或更多预定的科学或临床目的，利用观察性研究方法收集统一的数据来评估某一特定疾病、状况或暴露人群的结局指标，其结论可为描述疾病的自然史或确定某一治疗措施的临床疗效、安全性、成本效益以及评价或改善临床治疗提供科学依据 
>
>疾病登记处是一个数据库，用于跟踪特定疾病的发病率、治疗方法和治疗反应。登记册可由大型实体维护，如医院或政府机构，或者由私人医生利用循证治疗方法。从疾病登记处收集的信息有助于确定病因，传播模式和治疗效果。制药公司还使用注册处收集的数据来跟踪患者的反应并调整风险因素。
>
>
>
>这张图就是一个常见的disease register的例子
>
>左边的是：
>
>baseline characteristics for every individual in your dataset, such as: demographic information, genetic information, RNA sequencing data,.
>
>右上角的红框：
>
>下面的两个是药物，上面的三个line是治疗策略，比如医生治病，会先使用第一种方法，两个药物联用，然后不管用后，用line 2的疗法，只用下面的那种药物，还不行的话就换line 3+，上下对照着看。
>
>右下角的黄框：
>
>实验室的结果

![image-20220827194808152](Lecture%2021%20EHRs%20and%20data%20mining.assets/image-20220827194808152.png)

>生物标志物（Biomarker）是指可以标记系统、器官、组织、细胞及 亚细胞 结构或功能的改变或可能发生的改变的生化指标，具有非常广泛的用途。 生物标志物可用于疾病诊断、判断疾病分期或者用来评价新药或新疗法在目标人群中的安全性及有效性。
>
>这个图里面只放了一种biomarker，但是实际上我们往往使用多种biomarker，X是高维的数据。这里面的一个$X_i$是一个患者，外面希望我们建立的模型让这个似然函数最大。

![image-20220827195739923](Lecture%2021%20EHRs%20and%20data%20mining.assets/image-20220827195739923.png)