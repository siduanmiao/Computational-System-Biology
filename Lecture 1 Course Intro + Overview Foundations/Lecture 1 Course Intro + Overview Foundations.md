The study procedure : Video+slides,  Goodfellow Chapter 1, Course materials

# Video+slides

## **Generative and discriminative machine**

**Algorithms of this type try to model “how to populate the dataset.”** Sampling the model gives generated, synthetic data points.

We estimate the probability distributions. Formally, the generative model estimates the conditional probability ![P(X|Y=y)](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-4a7378eea895d4acf4760afea69dc704_l3.svg) for a given target ![y](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-38461fc041e953482219abf5d4cce1cb_l3.svg). For example, the Naive Bayes algorithm models ![P(x, y)](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-97942be636609bd29660ee1f0a722619_l3.svg) and then transforms the probabilities into conditional probabilities ![P(y|x)](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-52f1e9c7f92805dfdcbe770ec33c73d2_l3.svg) by applying the Bayes rule.

Some popular generative algorithms are:

- [Naive Bayes](https://www.baeldung.com/cs/naive-bayes-classification) Classifier
- Generative Adversarial Networks
- Gaussian Mixture Model
- Hidden Markov Model
- Probabilistic context-free grammar

**Discriminative algorithms focus on modeling a direct solution.** For example, the logistic regression algorithm models a decision boundary. Then it decides on the outcome of an observation based on where it stands relative to the decision boundary.

Discriminative algorithms estimate posterior probabilities. Unlike the generative algorithms, they don’t model the underlying probability distributions. Formally, we model the conditional probability of target ![Y](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-42ae22abcaa05c2d6c2fdc3746446019_l3.svg) ![P(Y|X=x)](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-485c5582f7e8ac17397249e1983a6238_l3.svg) given an observation ![x](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-7e5fbfa0bbbd9f3051cd156a0f1b5e31_l3.svg).

Some popular discriminative algorithms are:

- k-nearest neighbors (k-NN)
- Logistic regression
- [Support Vector Machines](https://www.baeldung.com/cs/ml-support-vector-machines) (SVMs)
- Decision Trees
- Random Forest
- Artificial Neural Networks (ANNs)

**The generative approach focuses on modeling, whereas the discriminative approach focuses on a solution.** So, we can use generative algorithms to generate new data points. Discriminative algorithms don’t serve that purpose.

**Still, discriminative algorithms generally perform better for classification tasks.** That’s because they focus on solving the actual problem directly instead of solving a more general problem first.

**Yet, the real strength of generative algorithms lies in their ability to express complex relationships between variables.** In other words, they have explanatory power. As a result, they have successful use cases in NLP and medicine.

![img](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/gen_vs_disc-versus-1.png)

![Rendered by QuickLaTeX.com](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/quicklatex.com-42db9c8d268c78bc42ac756aed6f9f45_l3.svg)

# Goodfellow Chapter 1

This is the introduction of AI,the follow content of the book:

* Part I introduces basic mathematical tools and machine learning concepts. 

* Part II describes the most established deep learning algorithms, which are essentially solved technologies. 

* Part III describes more speculative ideas that are widely believed to be important for future research in deep learning.

![image-20220802144943642](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802144943642.png)

## What is AI

Abstract and formal tasks that are among the most diﬃcult mental undertakings for a human being are among the easiest for a computer.

![image-20220802094032184](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802094032184.png)

**knowledge base**: Several artiﬁcial intelligence projects have sought to hard-code knowledge about the world in formal languages. A computer can reason automatically about statements in these formal languages using logical inference rules. For example: Cyc project.

This is a hard-code. **Hard coding** (also **hard-coding** or **hardcoding**) is the software development practice of embedding data directly into the [source code](https://en.wikipedia.org/wiki/Source_code) of a [program](https://en.wikipedia.org/wiki/Computer_program) or other executable object, as opposed to obtaining the data from external sources or generating it at [runtime](https://en.wikipedia.org/wiki/Run_time_(program_lifecycle_phase)). Thus, all knowledge is set by people.

**machine learning**: The difficulties faced by systems relying on hard-coded knowledge suggest that AI systems need the ability to acquire their own knowledge, by extracting patterns from raw data. This capability is known as machine learning. The introduction of machine learning enabled computers to tackle problems involving knowledge of the real world and make decisions that appear subjective. For example: Naive Bayes, Logistic regression. The performance of these simple machine learning algorithms depends heavily on the representation of the data(**feature**) they are given. However, it cannot inﬂuence how features are deﬁned in any way.

The **choice of representation** has an enormous effect on the performance of machine learning algorithms.

![image-20220802100412835](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802100412835.png)

**representation learning**: One solution to this problem is to use machine learning to discover not only the mapping from representation to output but also the representation itself. Learned representations often result in much better performance than can be obtained with hand-designed representations.

![image-20220802103014777](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802103014777.png)

For example: The quintessential example of a representation learning algorithm is the **autoencoder**. An autoencoder is the combination of an encoder function, which converts the input data into a different representation, and a decoder function,which converts the new representation back into the original format.

![image-20220802103808517](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802103808517.png)

Autoencoders are trained to preserve as much information as possible when an input is run through the encoder and then the decoder, but they are also trained to make the **new representation** have various nice properties.

When designing features or algorithms for learning features, our goal is usually to separate the **factors of variation** that explain the observed data. Such factors are often not quantities that are directly observed. Instead, they may exist as either **unobserved objects or unobserved forces** in the physical world that affect observable quantities

Of course, it can be very difficult to extract such high-level, abstract features from raw data. Many of these factors of variation, such as a speaker’s accent, can be identiﬁed only using sophisticated, nearly human-level understanding of the data. When it is nearly **as difficult to obtain a representation as to solve the original problem**, representation learning does not, at ﬁrst glance, seem to help us.

**Deep learning**: solves this central problem in representation learning by introducing representations that are expressed in terms of other, simpler representations. Deep learning enables the computer to **build complex concepts out of simpler concepts**.

![image-20220802111008740](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802111008740.png)

>Learning or evaluating this mapping seems insurmountable if tackled directly. Deep learning resolves this diﬃculty by breaking the desired complicated mapping into a series of nested simple mappings, each described by a diﬀerent layer of the model. The input is presented at the **visible layer**, so named because it contains the variables that we are able to observe. Then a series of **hidden layers** extracts increasingly abstract features from the image. These layers are called “hidden” because their values are not given in the data; instead the model must determine which concepts are useful for explaining the relationships in the observed data. The images here are visualizations of the kind of feature represented by each hidden unit. Given the pixels, the ﬁrst layer can easily **identify edges**, by comparing the brightness of neighboring pixels. Given the ﬁrst hidden layer’s description of the edges, the second hidden layer can easily search for **corners and extended contours**, which are recognizable as collections of edges. Given the second hidden layer’s description of the image in terms of corners and contours, the third hidden layer can detect **entire parts of speciﬁc objects**, by ﬁnding speciﬁc collections of contours and corners. Finally, this description of the image in terms of the object parts it contains can be used to recognize the objects present in the image.

For example: multilayer perceptron (MLP). We can think of each application of a different mathematical function as providing a new representation of the input.

The idea of learning the right representation for the data provides **one perspective** on deep learning. **Another perspective** on deep learning is that depth enables the computer to learn a multistep computer program.

There are two main ways of measuring the depth of a model.

1. The ﬁrst view is based on the number of sequential instructions that must be executed to evaluate the architecture.

Just as two equivalent computer programs will have different lengths depending on which language the program is written in, the **same function may be drawn as a ﬂowchart with different depths** depending on which functions we allow to be used as individual steps in the ﬂowchart.

![image-20220802142226060](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802142226060.png)

>Illustration of computational graphs mapping an input to an output where each node performs an operation. Depth is the length of the longest path from input to output but depends on the deﬁnition of what constitutes a possible computational step.
>
>The computation depicted in these graphs is the output of a logistic regression model,σ(wTx), where σ is the logistic sigmoid function. If we use addition, multiplication and logistic sigmoids as the elements of our computer language, then this model has depth three. If we view logistic regression as an element itself, then this model has depth one.

2. Another approach, used by deep probabilistic models, regards the depth of a model as being not the depth of the computational graph but the depth of the graph **describing how concepts are related to each other**.

In this case, the depth of the ﬂowchart of the computations needed to compute the representation of each concept may be much deeper than the graph of the concepts themselves. This is because the system’s understanding of the simpler concepts can be **reﬁned** given information about the more complex concepts. 

For example, an AI system observing an image of a face with one eye in shadow may initially see only one eye. After detecting that a face is present, the system can then infer that a second eye is probably present as well. In this case, the graph of concepts includes only two layers—a layer for eyes and a layer for faces—but the graph of computations includes 2n layers if we **reﬁne our estimate of each concept given the other** n times

**Summary**

1. Concept

   ![image-20220802144605578](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802144605578.png)

>A Venn diagram showing how deep learning is a kind of representation learning, which is in turn a kind of machine learning, which is used for many but not all approaches to AI. Each section of the Venn diagram includes an example of an AI technology

2. Flowcahrt

   ![image-20220802144711864](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802144711864.png)

>Flowcharts showing how the diﬀerent parts of an AI system relate to each other within diﬀerent AI disciplines. Shaded boxes indicate components that are able to learn from data

## The history of AI( just for understanding)

In fact, deep learning dates back to the 1940s.

![image-20220802152946639](Lecture%201%20Course%20Intro%20+%20Overview%20Foundations.assets/image-20220802152946639.png)

>Two of the three historical waves of artiﬁcial neural nets research, as measured by the frequency of the phrases “cybernetics” and “connectionism” or “neural networks,” according to Google Books (the third wave is too recent to appear). The ﬁrst wave started with cybernetics in the 1940s–1960s, with the development of theories of biological learning (McCulloch and Pitts, 1943; Hebb, 1949) and implementations of the ﬁrst models, such as the perceptron (Rosenblatt, 1958), enabling the training of a single neuron. The second wave started with the connectionist approach of the 1980–1995 period, with backpropagation (Rumelhart et al., 1986a) to train a neural network with one or two hidden layers. The current and third wave, deep learning, started around 2006 (Hinton et al., 2006; Bengio et al., 2007; Ranzato et al., 2007a) and is just now appearing in book form as of 2016. The other two waves similarly appeared in book form much later than the corresponding scientiﬁc activity occurred

Some of the earliest learning algorithms we recognize today were intended to be computational models of biological learning, that is, models of how learning happens or could happen in the brain. As a result, one of the names that deep learning has gone by is **artiﬁcial neural networks (ANNs).**

The ﬁeld of **deep learning** is primarily concerned with how to build computer systems that are able to successfully solve tasks requiring intelligence, while the ﬁeld of **computational neuroscience** is primarily concerned with building more accurate models of how the brain actually works. 

In the 1980s, the second wave of neural network research emerged in great part via a movement called connectionism , or parallel distributed processing. Several key concepts arose during the connectionism movement of the 1980s that remain central to today’s deep learning:

1. **distributed representation**: This is the idea that each input to a system should be represented by many features, and each feature should be involved in the representation of many possible inputs. For example, suppose we have a vision system that can recognize cars, trucks, and birds, and these objects can each be red, green, or blue. One way of representing these inputs would be to have a separate neuron or hidden unit that activates for each of the nine possible combinations: red truck, red car, red bird, green truck, and so on. This requires nine diﬀerent neurons, and each neuron must independently learn the concept of color and object identity. One way to improve on this situation is to use a distributed representation, with three neurons describing the color and three neurons describing the object identity. This requires only six neurons total instead of nine, and the neuron describing redness is able to learn about redness from images of cars, trucks and birds, not just from images of one speciﬁc category of objects.

2. **back-propagation**

During the 1990s, researchers made important advances in modeling sequences with neural networks. the long short-term memory (LSTM) network to resolve some of these diﬃculties. Today, the LSTM is widely used for many sequence modeling tasks

The second wave of neural networks research lasted until the mid-1990s, two factors led to a decline in the popularity of neural networks that lasted until 2007

1. Ventures based on neural networks and other AI technologies began to make unrealistically ambitious claims while seeking investments. When AI research did not fulﬁll these unreasonable expectations, investors were disappointed. 
2. Simultaneously,other ﬁelds of machine learning made advances. Kernel machines and graphical models both achieved good results on many important tasks.

The third wave of neural networks research began with a breakthrough in 2006. Geoﬀrey Hinton showed that a kind of neural network called a deep belief network could be eﬃciently trained using a strategy called greedy layer-wise pretraining. This wave of neural networks research popularized the use of the term “deep learning” to emphasize that researchers were now able to train deeper neural networks than had been possible before, and to focus attention on the theoretical importance of depth

The third wave began with a focus on new unsupervised learning techniques and the ability of deep models to generalize well from small datasets, but today there is more interest in much older supervised learning algorithms and the ability of deep models to leverage large labeled datasets.



