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