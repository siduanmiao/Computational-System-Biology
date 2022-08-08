# Vedio

## Introduction

generative model: create stuff in the world and actually model the world, not just discriminate.

Such as :**GANs**(Generative Adversarial Networks), **VAEs**(Variational Autoencoder)

And, how do models learn representations.

![image-20220808190036139](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808190036139.png)

![image-20220808190438971](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808190438971.png)



![image-20220808190936778](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808190936778.png)

And, what is **latent space**?

If I have to describe latent space in one sentence, it simply means a **representation of compressed data.**

![image-20220808192941055](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808192941055.png)

![image-20220808193044785](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808193044785.png)

![image-20220808193104672](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808193104672.png)

Suddenly, we can use self-supervised learning. this is not quite the same as unsupervised learning, unsupervised learning basically says find some clustering these data but self-supervised learning says **i'm going to make some classification tasks or some prediction tasks or some supervised task by exploiting ** just the data and tricking the data into being its own supervisor so it's not quite unsupervised but it's not quite supervised either. it's self-supervised where you're using part of the data as training for other part of the data with the explicit goal of **learning very cool representations and why our representation is cool**. because you can use representations to generate views of the world. you can basically **run the model backwards** and basically say given a latent space representation (given a set of vectors that basically tells me i see headlights and i see a rotational pose and i see you know an older person etc, because in CNN we learn these features in latent space) can i vary these vectors and then generate images by basically going backwards through this architecture(the red area) and then having expansions of these **compressed  representation of the world** into **examples of the world**. so that's what the generative models are adding the model backwards and effectively going from z to more examples of x.

**So how can we learn representation without annotation**

![image-20220808200523331](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808200523331.png)

1. in the context of recurrent neural networks we we saw one example of using self-supervision as a way to learn representations and the self-supervision was constantly predicting what's next. in the  world, basically using the time series nature of speech data or video data or any kind of input that we're receiving from the world using the temporal aspect of that as a way to learn a representation that captures something meaningful about the world and then predicts the next item so in video or in speech or in any kind of textual you can actually **predict the future**

2. First we should know what is **Pretext task**, also can be seen as a self-supervised task.

   ![image-20220808201436683](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808201436683.png)

   * **Predict self** : Autoencoder, to learn the representation of x. 

     ![image-20220808202056085](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808202056085.png)

   * before/after

     ![image-20220808202619836](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808202619836.png)

   * missing patch

     ![image-20220808202650706](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808202650706.png)

   * correct rotation

     ![image-20220808202713214](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808202713214.png)

   * clorization

     ![image-20220808202600173](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808202600173.png)

3.  AE 

4.  VAE 
5.  what is the **Orthogonalization**
6.  GAN

So previous content is an introduction, and we're going to follow this course

## pretext task

![image-20220808205236635](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808205236635.png)

The good thing is, in the world, we have a lot of input data but a little bit of it has labels on it, and we can greatly amplify the data that we can use to learn.

## Auto-Encoder

![image-20220808211636432](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808211636432.png)

![image-20220808211829370](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808211829370.png)

![image-20220808211903036](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220808211903036.png)

![image-20220809003423791](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809003423791.png)

We can use encoder and decoder separately for different tasks:

decoder: as a generative model

encoder: feature space vector representation learning that i can use to compare how similar are the different images to each other. or find the variation of different images to do projections

![image-20220809003535727](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809003535727.png)

It seems like to CNN, but we initial the encoder using autoencoder and we link it with predicted layer.

## VAE

as usual we use the website to learn the basic knowledge of it

![image-20220809004749779](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809004749779.png)

![image-20220809004810913](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809004810913.png)

~~~http
https://zhuanlan.zhihu.com/p/452743042
~~~

