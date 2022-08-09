

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

And we talk about **KL divergence**

![image-20220809093905438](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809093905438.png)

Then we talk about VAE

![image-20220809095142103](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809095142103.png)

![image-20220809100140527](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809100140527.png)

![image-20220809102503330](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809102503330.png)

![image-20220809102727536](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809102727536.png)

![image-20220809104609446](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809104609446.png)

![image-20220809110821650](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809110821650.png)

**直接优化似然函数比较困难，因此我们考虑转而优化似然函数的下界**

![image-20220809110935460](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809110935460.png)

![image-20220809111018507](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111018507.png)

![image-20220809111125842](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111125842.png)

![image-20220809111317712](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111317712.png)

![image-20220809111324460](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111324460.png)

>using simple words to explain:
>
>![image-20220809141721132](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809141721132.png)
>
>![image-20220809135117399](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809135117399.png)
>
>![image-20220809134807798](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809134807798.png)



![image-20220809111600512](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111600512.png)

![image-20220809111903312](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809111903312.png)

![image-20220809112032455](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809112032455.png)



![image-20220809134825823](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809134825823.png)

![image-20220809134102888](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809134102888.png)

![image-20220809134138523](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809134138523.png)

![image-20220809134409281](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809134409281.png)



Then we back to our vedio:

![image-20220809115936185](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809115936185.png)

![image-20220809115954051](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809115954051.png)

![image-20220809120154919](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809120154919.png)

![image-20220809120541871](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809120541871.png)

![image-20220809120712516](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809120712516.png)

For examples:

given a bunch of pixels, I'm recognizing a boat and some variation about the boat and a generation network which basically says given that i know that there's a boat it has a length it has a scale it has a size an orientation etc, I'm generating uh images from that underlying representation

![image-20220809121426573](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809121426573.png)

![image-20220809121509422](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809121509422.png)

![image-20220809121630386](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809121630386.png)

![image-20220809131312793](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809131312793.png)

![image-20220809131528892](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809131528892.png)

![image-20220809131850100](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809131850100.png)

![image-20220809132512872](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809132512872.png)

## The ideas contained in the VAE

![image-20220809140527250](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809140527250.png)

![image-20220809140957767](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809140957767.png)

![image-20220809141037367](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809141037367.png)

![image-20220809141112766](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809141112766.png)

![image-20220809141207454](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809141207454.png)

## GAN

![image-20220809154146076](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809154146076.png)

We can see that the output of our generative model is not so good and we want to improve it. One possible method is we hire some people providing feedback of your output and let you improve your model to fake them. We use the NN as these people for evaluation.

![image-20220809160123500](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809160123500.png)

![image-20220809161852375](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809161852375.png)

As usual, I start it by searching on the website to have a basic understand of GAN:

![image-20220809162430351](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809162430351.png)

![image-20220809163303652](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809163303652.png)

![image-20220809163516142](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809163516142.png)

![image-20220809163712274](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809163712274.png)

![image-20220809165151375](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165151375.png)

![image-20220809165237551](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165237551.png)

![image-20220809165333048](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165333048.png)

![image-20220809165439977](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165439977.png)

![image-20220809165506895](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165506895.png)

![image-20220809165634758](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165634758.png)

![image-20220809165712059](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165712059.png)

So we back to the vedio:

![image-20220809165904848](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809165904848.png)

![image-20220809183927848](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809183927848.png)

![image-20220809184306841](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809184306841.png)

![image-20220809184451406](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809184451406.png)

We use MSE before to evaluate the $\hat x$ and x, but it is sometimes bad, and our GAN is greater than it.



![image-20220809184754909](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809184754909.png)

## DGCNN: GAN + CNN

![image-20220809190019750](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809190019750.png)

![image-20220809191512109](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809191512109.png)

![image-20220809191536383](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809191536383.png)

![image-20220809191609482](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809191609482.png)

![image-20220809191657695](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809191657695.png)

![img](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/1439869-20200709142052548-1574172421.gif)

![image-20220809192057605](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809192057605.png)

![image-20220809192145312](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809192145312.png)

![image-20220809193801726](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809193801726.png)

![image-20220809194144153](Lecture%206%20Generative%20Models,%20GANs,%20VAE.assets/image-20220809194144153.png)

that the power of deep learning doesn't come from the x and the y or the fully connected layer, the power of deep learning really comes from the latent space representation learning
