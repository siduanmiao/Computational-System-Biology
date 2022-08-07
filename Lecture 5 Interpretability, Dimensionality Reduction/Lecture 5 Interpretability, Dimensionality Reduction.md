# Vedio

![image-20220807193622395](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807193622395.png)

What are the tricks and what are the insight that we can learn from good deep learning model?

**We want to learn from the Deep learning models**

![image-20220807194244091](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807194244091.png)

![image-20220807194527219](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807194527219.png)

![image-20220807195024394](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807195024394.png)

![image-20220807195130326](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807195130326.png)

![image-20220807200724924](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807200724924.png)

![image-20220807201725579](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807201725579.png)

![image-20220807201310951](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807201310951.png)

![image-20220807202302751](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807202302751.png)

When it comes to interpreting models:

![image-20220807202354503](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807202354503.png)

![image-20220807202503319](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807202503319.png)

Sometimes there are thousands of layers and millions of parameters, so can dive deeper.

![image-20220807203719448](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807203719448.png)

![image-20220807204109575](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807204109575.png)

 ![image-20220807211834169](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807211834169.png)

![image-20220807204450599](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807204450599.png)

Because the model is mature, we should use the parameters of model and can't change the model. We just want to interpret it. We just want to find a input that maximizes the posterior probability of being assigned to a particular class

**If we just use the Class Probability**:

![image-20220807204700554](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807204700554.png)

![image-20220807204839364](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807204839364.png)

![image-20220807204903289](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807204903289.png)

![image-20220807205054237](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807205054237.png)

![image-20220807210242380](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807210242380.png)

![image-20220807210259092](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807210259092.png)

![image-20220807210317891](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807210317891.png)

we can add more constraint about it:

For expert: we know the original probability density of  the input :$p(x)$

For Code Space: we know the method $g(z)$ that product the x. so we can use $g(z)$ to replace x in the formula. 

![image-20220807210737826](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807210737826.png)

![image-20220807210847676](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807210847676.png)

![image-20220807213005711](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807213005711.png)

![image-20220807213042467](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807213042467.png)

![image-20220807214325446](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220807214325446.png)

We select particular examples for both prototype images and also prototype criticisms which are the most informative distinguishing that particular class

![image-20220808001339329](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220808001339329.png)

![image-20220808001633971](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220808001633971.png)



![image-20220808001919469](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220808001919469.png)

![image-20220808002356528](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220808002356528.png)

![image-20220808002928706](Lecture%205%20Interpretability,%20Dimensionality%20Reduction.assets/image-20220808002928706.png)