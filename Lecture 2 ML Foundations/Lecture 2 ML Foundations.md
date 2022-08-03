# Vedio

The Notation of this class:

![image-20220803104955901](Lecture%202%20ML%20Foundations.assets/image-20220803104955901.png)

![image-20220803105303748](Lecture%202%20ML%20Foundations.assets/image-20220803105303748.png)

the function is non-linear to approximate any functions.

![image-20220803144044487](Lecture%202%20ML%20Foundations.assets/image-20220803144044487.png)

for discriminative model we only try to find $P(Y|X)$, rather than the $P(X,Y)$, so we just can judge rather than generate.

![image-20220803145708897](Lecture%202%20ML%20Foundations.assets/image-20220803145708897.png)

In this class, the notation is 
$$
Y=R^k
$$
means: the value range is R, and it is a vector of k dimensions

such as :
$$
(1,2,2,2,1...)_k
$$
Objective function:

![image-20220803152758372](Lecture%202%20ML%20Foundations.assets/image-20220803152758372.png)

KL divergence: the difference between two distribution

Prior probability: based on previous experience and analysis. A probability that can be obtained before the experiment or sampling.

Posterior probability: The probability that an event has occurred and that the reason for the event is to be calculated by a factor.

![image-20220803153607350](Lecture%202%20ML%20Foundations.assets/image-20220803153607350.png)

regularizers and constraints: to avoid over-fit and more likely to generalize.

penalize the total sum of all of our paprameters, for L1: absolute, for L2: for square.

negative log-likelihood:

![image-20220803154448798](Lecture%202%20ML%20Foundations.assets/image-20220803154448798.png)

![image-20220803154623548](Lecture%202%20ML%20Foundations.assets/image-20220803154623548.png)

Loss function for classification:

![image-20220803154032682](Lecture%202%20ML%20Foundations.assets/image-20220803154032682.png)

binary cross-entropy is derived from the Bernoulli distribution

![image-20220803161341777](Lecture%202%20ML%20Foundations.assets/image-20220803161341777.png)

we want to make the P(D) max, but for loss function we should let it min, so we use NLL to change it.

for muti-class classfication

![image-20220803164223952](Lecture%202%20ML%20Foundations.assets/image-20220803164223952.png)

loss function for regression:

![image-20220803171037452](Lecture%202%20ML%20Foundations.assets/image-20220803171037452.png)

probability density function of Gaussian is:

![image-20220803171805033](Lecture%202%20ML%20Foundations.assets/image-20220803171805033.png)

the likelihood log function is:

![image-20220803171907152](Lecture%202%20ML%20Foundations.assets/image-20220803171907152.png)

Both methods give the same result, so from the perspective of probability, MSE is based on the assumption of Gaussian distribution.

![image-20220803173243969](Lecture%202%20ML%20Foundations.assets/image-20220803173243969.png)

**The loss under the average meaning of the joint distribution P(X,Y) of the theoretical model F (X)** is called risk function or expected loss.

In a word, the average loss function is the risk function

**empirical risk**: Empirical risk is the average loss (value of loss function) of model F (X) on the **training dataset**, also known as empirical loss.

![img](Lecture%202%20ML%20Foundations.assets/1174145-20170828141212577-1125011174.png)

**expected risk**: The expected risk is the average loss of model F (X) on **all data sets**. All the data sets here include training set, validation set, and possibly unknown test set.

![img](Lecture%202%20ML%20Foundations.assets/1174145-20170828143844593-63634644.png)

**structural risk**: "Structural risk" is a compromise between "empirical risk" and "expected risk". Structural risk is empirical risk plus regularization term. 

![img](Lecture%202%20ML%20Foundations.assets/1174145-20170828145956015-1837068530.png)

**empirical risk minimization,ERM**:

![image-20220803184603124](Lecture%202%20ML%20Foundations.assets/image-20220803184603124.png)

**Structural Risk Minimization, SRM**

![image-20220803184614456](Lecture%202%20ML%20Foundations.assets/image-20220803184614456.png)

objective function is the target function, it can be loss function , risk function and so on.

![image-20220803193558794](Lecture%202%20ML%20Foundations.assets/image-20220803193558794.png)

![image-20220803194311335](Lecture%202%20ML%20Foundations.assets/image-20220803194311335.png)

![image-20220803195818550](Lecture%202%20ML%20Foundations.assets/image-20220803195818550.png)

![image-20220803200410228](Lecture%202%20ML%20Foundations.assets/image-20220803200410228.png)

for regression:

![image-20220803200655796](Lecture%202%20ML%20Foundations.assets/image-20220803200655796.png)

![image-20220803200840317](Lecture%202%20ML%20Foundations.assets/image-20220803200840317.png)

![image-20220803201105991](Lecture%202%20ML%20Foundations.assets/image-20220803201105991.png)

This is the statistic question and we test the significance of the correlation.

![image-20220803201505085](Lecture%202%20ML%20Foundations.assets/image-20220803201505085.png)

![image-20220803201716803](Lecture%202%20ML%20Foundations.assets/image-20220803201716803.png)

![image-20220803235707279](Lecture%202%20ML%20Foundations.assets/image-20220803235707279.png)

lack of correlation not equal to lack of relationship. All the photos ahead have near zero correlation but have strong relationship.

![image-20220804000241546](Lecture%202%20ML%20Foundations.assets/image-20220804000241546.png)

![image-20220804000743851](Lecture%202%20ML%20Foundations.assets/image-20220804000743851.png)

![image-20220804001207022](Lecture%202%20ML%20Foundations.assets/image-20220804001207022.png)

How can we adapt the parameters in the network?

**through the partial derivatives of the error with respect to each of the input variables**

![image-20220804001719643](Lecture%202%20ML%20Foundations.assets/image-20220804001719643.png)

![image-20220804003413536](Lecture%202%20ML%20Foundations.assets/image-20220804003413536.png)

**model capacity:**The capacity (Vapnik-Chervonenkis dimension) of a model describes how many points can be correctly predicted when they are produced by an adversary

![image-20220804004652697](Lecture%202%20ML%20Foundations.assets/image-20220804004652697.png)

The **generalizability** of a model describes its ability to perform well on **previously unseen inputs**

![image-20220804005939486](Lecture%202%20ML%20Foundations.assets/image-20220804005939486.png)

more neurons = more capacity

We can reduce the capacity of our model to avoid overfitting but the challenge is if we reduce the capacity, we also reduce the space of possible functions that we could  approximate.

So another way is to simply regularize our parameters by penalizing the magnitudes of these parameters.

![image-20220804010548221](Lecture%202%20ML%20Foundations.assets/image-20220804010548221.png)