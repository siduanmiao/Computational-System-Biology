# Vedio

## Introduction

For CNN, we try to **see**

For RNN, we try to read, listen, understand and write.

NLP: Natural Language Processing 

![image-20220805121043535](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805121043535.png)

In RNN, we try to give it the ability of predicting the next as people do.

"When we listen to someone talking, the change in our brain's processing from not caring what kind of sound it is to recognizing it as a word happens surprisingly early," said Simon.   "In fact, this happens pretty much as soon as the linguistic information becomes available."  When it is engaging in speech perception, the brain's auditory cortex analyzes complex acoustic patterns to detect words that carry a linguistic message.   It seems to do this so efficiently, at least in part, by anticipating what it is likely to hear: by learning what sounds signal language most frequently, **the brain can predict: what may come next.**   It is generally thought that this process localized bilaterally in the brain's superior temporal lobes involves recognizing an intermediate, phonetic level of sound.

![image-20220805155005194](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805155005194.png)

![image-20220805155351003](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805155351003.png)

In probability and statistics, memorylessness is a property of certain probability distributions:  the probabilities would not be influenced by the history of the process

In the context of Markov processes, memorylessness refers to the Markov property,an even stronger assumption which implies that the properties of **random variables related to the future** depend only **on relevant information about the current time,** not on information from further in the past. 

**Autoregression:** 

![image-20220805155750856](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805155750856.png)

![image-20220805160230976](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805160230976.png)

**we can see that the two memoryless models just use the former input to predict, what about add the hide stat to make it more powerful!****

There are only two hidden state models that are computationally feasible, which are briefly described next. The purpose of the introduction is to compare with the RNN, not to learn it itself: 

**Linear Dynamical Systems** and **HMM**

![image-20220805161141524](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805161141524.png)

![image-20220805161300560](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805161300560.png)

The hidden state of HMM is **discrete**, while the hidden state of Linear Dynamic System is **continuous**

LDS:

![img](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/format,png-16596873679223.png)

![img](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/format,png.png)

**Successive hidden states directly determine the output** in LDS.

But in HMM, the hidden stat can't determine the output, just give a probability.

HMM: emission matrix and transition matrix

![image-20220805165327707](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805165327707.png)

This part did not find the explanation, temporarily doubtful, my personal understanding is:

![image-20220805170600805](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805170600805.png)

The biggest advantage of RNN is that it can really **make full use of all the above information** to predict the next word, unlike HMM, which can only open a window of N words and only use the first N words to predict the next word. Formally, this is a very "ultimate" model, after all, he uses all the information that can be used in a language model

## RNN

![image-20220805183649554](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805183649554.png)

Before we get to the language input model we need to encode

**word embeddings = word vectors :**

It can encode the similarities and differences between words into word vectors

* similarity: the words with similar meaning should be closer in vector space
* differences: the words with different meaning should be far in vector space

There are two common encoding methods: **one-hot Representation** and **Distributed Representation.**

**Hidden state representation: HMM is one hot, RNN is distributed representation.**

**one-hot vector**

![image-20220805184605990](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805184605990.png)

![image-20220805184613633](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805184613633.png)

**Distributed Representation** 

![image-20220805192126155](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805192126155.png)



**Word2vec**:

![image-20220805191509604](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805191509604.png)

We don't need to know the meaning of this vector, it is just a suitable representation of words produced by computer.

![image-20220805191634631](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805191634631.png)

![image-20220805192328608](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805192328608.png)

This is the model of RNN

![image-20220806174544824](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806174544824.png)

![image-20220806174506525](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806174506525.png)

![image-20220806174707356](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806174707356.png)

The RNN will memorize all the sequential information we learned earlier

![image-20220805193825914](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805193825914.png)

The previous diagram is a simplified model, the actual model is as follows

![image-20220807003143312](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807003143312.png)

**STOCHASTIC MODELS**

A stochastic model is the one that recognizes the random nature of the variables.The output is only an estimate of the nature of the model with given set of inputs. Software is run several times to **give a distribution of results of the model**.

**DETERMINISTIC MODEL**

A model that doesn’t contain any random variable is a deterministic model.A deterministic model is a special kind of stochastic model with zero randomness. In a deterministic model **a single output is obtained with a fixed series of inputs**

![image-20220805194825742](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805194825742.png)

For LDS: the noise

For HMM: the probability of the two metrics.

When we have a particular sequence, we know exactly **what the posterior probability distribution of the hidden state** will be given an observable sequence

By simply unrolling the time, we can see the equivalence between **feed forward net using same weight of each layer** and RNN

![image-20220805201317593](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805201317593.png)

**Multi-Layer Perceptron,MLP** = **feed forward net**

**Different RNN remembering architecture:**

1.  No output

![image-20220805202820210](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805202820210.png)

2. A single output after entire sequence

![image-20220805231949439](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220805231949439.png)

example:

I'm reading a big passage on twitter and then i'm trying to decide if the person is happy or angry or... I basically have this set of inputs that are being computed exactly the same way at every time so all of the weights are exactly identical as unrolled over time and in the end I have a Output function $o^{(t)}$and i may have a training corpus where I know the annotation of a bunch of tweets $y^{(t)}$, like happy, angry... and the loss function $L^{(t)}$ is the discrepancy between what I should predicting $y^{(t)}$ and what i am predicting $o^{(t)}$ in my network. Then I can train my network using exactly the same tools that we've seen so far: using back propagation to update the weights.

But what's really cool is that you're updating the weights which are shared at all of these different levels(different layers of different time)

3. many output

![image-20220806003832670](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806003832670.png)



![image-20220806180304695](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806180304695.png)



![image-20220806180716271](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806180716271.png)

4. output -> hidden

![image-20220806004320438](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806004320438.png)

5. label output -> hidden

![image-20220806004419606](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806004419606.png)





BPTT: back-propagation through time

![image-20220806005326969](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806005326969.png)

![image-20220806005429507](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806005429507.png)

We do that to meet the **weight constraint that all the weight are same for all layers.**

The **vanishing gradient** in the RNN does not mean that the total gradient of the loss to the parameter disappears, but that the gradient of the RNN to the far time step disappears. The back propagation through time(BPTT) method is used in RNN. The gradient of **loss with respect to parameter W** is equal to **the sum of the derivatives of loss with respect to W at each time step**. Expressed as a formula(based on naive RNN):

![image-20220806010346063](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806010346063.png)

![image-20220806010459751](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806010459751.png)

If t minus j is very large, that is, j is very far away from t time steps, if $\sigma'W^h>1$, you have a gradient explosion problem, and if $\sigma'W^h<1$, you have a gradient vanishing problem. But when t minus j is small, which is the short-term dependence of t at j, there is no gradient disappearance/gradient explosion problem. Gradient clipping is generally used to solve the gradient explosion problem. Therefore, the vanishing gradient problem is mainly analyzed.

So the effect of j will decay to 0 if t is very far from it.

We can solve this by remembering inputs or intermediate variables over longer time periods. There are many ways to increase the length of the memory.

![image-20220806143557401](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806143557401.png)

ESN:

![image-20220806144202435](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806144202435.png)

![image-20220806144224078](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806144224078.png)

## LSMT

Therefore, we use **Long short-term memory(LSMT)** to deal with this question.

For now, let’s just try to get comfortable with the notation we’ll be using.

![image-20220806152614354](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806152614354.png)

In the above diagram, each line carries an entire vector(**We have known that the word should be encoded for train, and they will be encoded to a vector**), from the output of one node to the inputs of others. The pink circles represent pointwise operations, like vector addition, while the yellow boxes are learned neural network layers. Lines merging denote concatenation, while a line forking denote its content being copied and the copies going to different locations.

**The following formula we ignore the bias**

For simple RNN:

![image-20220806153321459](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806153321459.png)

In standard RNNs, this repeating module will have a very simple structure, **such as a single tanh layer.**

LSTMs also have this chain like structure, but the repeating module has a different structure. Instead of having a single neural network layer, **there are four, interacting in a very special way.**

**We add a carry track `C_t` to Simple RNN to carry information.** LSTM adds a method that can pass information several timesteps apart. Think of having a conveyor belt running together as you process sequences. Information at each point in time can be put on or taken off the conveyor belt, and you can also update the information on the conveyor belt. This preserves information from a long time ago and prevents it from being lost.

![image-20220806153443803](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806153443803.png)

we can see it in another way: the left is naive RNN and the right is LSTM

![img](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/v2-e4f9851cad426dfe4ab1c76209546827_720w.jpg)

![image-20220806160011929](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806160011929.png)

In there we use the two ways to present it and improve our understanding:

**Note: the $\sigma$ is sigmoid activation function**

![image-20220806162740772](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806162740772.png)

![image-20220806163528406](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806163528406.png)

![image-20220806163538413](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806163538413.png)

![image-20220806172105276](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806172105276.png)

## Attention +seq2seq

==we can use RNN and so on as a encoder and decoder!!==

Like seq2seq:

![image-20220806181022430](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806181022430.png)

![image-20220806181105123](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806181105123.png)

**Attention** is a signal processing mechanism discovered by scientists studying human vision in the 1990s. Practitioners in the field of artificial intelligence have introduced this mechanism into some models with success. At present, attention mechanism has become one of the most widely used "components" in deep learning, especially in natural language processing. In the past two years, **BERT, GPT, Transformer and other models or structures that have been highly exposed have adopted the attention mechanism.**

So, what is attention:

![image-20220806192847873](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806192847873.png)

For example, in basic seq2seq:

![image-20220806194106153](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806194106153.png)

![image-20220806194414143](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806194414143.png)

![image-20220806200001659](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806200001659.png)

![image-20220806203458008](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806203458008.png)

**Attention:**

![image-20220806200527425](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806200527425.png)

**There are other classification of the attention in the next article. I just use it as a primer**

For example:

![image-20220806204811563](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806204811563.png)

So, let's talk about the attention in this classification.

**This is a soft Attention**

![image-20220806203956968](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806203956968.png)

![image-20220806204112795](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806204112795.png)

![image-20220806204732583](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806204732583.png)

![image-20220806204748973](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806204748973.png)

So the soft attention can be summarized as

![image-20220806204932051](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806204932051.png)

**Hard Attention**

![image-20220806205048279](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806205048279.png)

**Global Attention\Local Attention**

![image-20220806205205190](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806205205190.png)

![image-20220806205243908](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806205243908.png)

Before we talk about the **self-attention**, we talk about the **Query-Key-Value**

![image-20220806205711906](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806205711906.png)

![image-20220806205741683](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806205741683.png)

![image-20220806210540767](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806210540767.png)

Now we can talk about the self attention:

![image-20220806210913943](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806210913943.png)

![image-20220806211127660](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211127660.png)

![image-20220806211211999](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211211999.png)

![image-20220806211329514](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211329514.png)

![image-20220806211451523](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211451523.png)

Another good interpretation:

![image-20220806211729503](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211729503.png)

![image-20220806211813812](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806211813812.png)

## Transformer

**The transformer is too hard for me now, later I will study it**:

~~~http
https://zhuanlan.zhihu.com/p/380426619
~~~

~~~http
https://zhuanlan.zhihu.com/p/467874444#:~:text=Transformer%E6%98%AF%E7%BA%AF%E7%B2%B9%E5%9F%BA%E4%BA%8E%E8%87%AA%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%9C%BA%E5%88%B6%E7%9A%84%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%EF%BC%8C%E5%AE%83%E5%9C%A8%E5%A4%84%E7%90%86%E5%BA%8F%E5%88%97%E9%97%AE%E9%A2%98%E4%B8%8A%E5%8F%96%E5%BE%97%E4%BA%86%E5%BC%95%E4%BA%BA%E6%B3%A8%E7%9B%AE%E7%9A%84%E6%88%90%E7%BB%A9%EF%BC%8C%E8%87%AA%E6%B3%A8%E6%84%8F%E5%8A%9B%E6%A8%A1%E5%9D%97%E4%B9%9F%E9%80%90%E6%B8%90%E6%88%90%E4%B8%BA%E4%BA%86%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B8%AD%E4%B8%8D%E5%8F%AF%E6%88%96%E7%BC%BA%E7%9A%84%E4%B8%80%E4%B8%AA%E5%BA%95%E5%B1%82%E6%A8%A1%E5%9D%97%E6%8B%BC%E5%9B%BE%EF%BC%8C%E4%B8%94%E6%98%AF%E7%9B%AE%E5%89%8D%E5%8F%91%E5%B1%95%E6%9C%80%E5%BC%BA%E5%8A%BF%E7%9A%84%E4%B8%80%E4%B8%AA%E6%A8%A1%E5%9D%97%EF%BC%8C%E5%AE%83%E5%9C%A8CNN%E3%80%81RNN%E6%93%85%E9%95%BF%E7%9A%84%E9%A2%86%E5%9F%9F%E6%94%BB%E5%9F%8E%E6%8E%A0%E5%9C%B0%EF%BC%8C%E7%94%9A%E8%87%B3%E5%AE%9E%E7%8E%B0%E4%BA%86%E8%B6%85%E8%B6%8A%E3%80%82,1.
~~~

## GNN

A good website to learn GNN

~~~http
https://distill.pub/2021/gnn-intro/
~~~

Then we will study the GNN:

![image-20220807104735862](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807104735862.png)



![image-20220807110517383](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807110517383.png)

But there are more complicated situation:

![image-20220807111858685](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807111858685.png)

![image-20220807112033335](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807112033335.png)

![image-20220807112339430](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807112339430.png)

So, how can we use this information (edge information + node information)

![image-20220807115656320](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807115656320.png)

* $O$ of the link information is $O(N)$, so if the nodes are too much, the input layer is very long
* if the number of nodes changes, the MLP model is hard to use the input with different length
* For a graph, the order of nodes is not a information because this the order we give to it, we can assume a node is "A" or "B", and it should node influent the result. But in this MLP model, if we change the order of nodes, the output will change. We can sort the order to deal with it, but it is too expensive.

So, we will talk about the basic formula of GNN.

![image-20220807121555569](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807121555569.png)



It seems not too difficult from what we see in CNN

![image-20220807122144612](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807122144612.png)

![image-20220807122255455](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807122255455.png)

We can extend this concept:

![image-20220807122825609](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807122825609.png)

We might aggregate them and then apply some non-linear function which makes this basically a little neural network.

The deep of GNN is not like the deep of MLP, CNN and so on. In MLP, we want to model higher order interactions between different parts of the input space. In GNN, we might actually getting more information overall because we actually entering into spaces of the graph.

![image-20220807123215420](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807123215420.png)

Each nodes defines its own subtree. There are many duplicated parts within subtrees. 

![image-20220807123838552](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807123838552.png)

In practice, there's nice **matrix-based representations of the GNN** updates that prevents us from actually duplicating this computation. 

![image-20220807124501739](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807124501739.png)

GCN is a graph convolutional neural network, which is a kind of GNN. The difference is mainly that the convolution operator is used for information aggregation. **GCN is mainly different from GNN in the aggregation step, which uses convolution**

![image-20220807132211328](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807132211328.png)

the $\sigma$ can be any function with can gradient back propagated through it.

assume that the length of vector of $h$ is $d$, so the dimension of $W$ is $d \times d$

**Desirable properties**

* The weight is shared by every update function of a specific layer, **every hidden layer have too weight: $W_1$ and $W_0$, one for neighbor and one for self.** 

* The update is  $O(E)$, because we apply this each time for each edge. Because even if you pass information  both from A->B and from B->A , it's only 2E 

Before we start the part 3, we talk about the inductive and transduction 

![image-20220807131405861](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807131405861.png)

![image-20220807131600651](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807131600651.png)

![image-20220807131526511](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807131526511.png)

![image-20220807131919418](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807131919418.png)

![image-20220807131952969](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807131952969.png)

**Limitations**

* Like LSTM we want the rnn to remember the long distance information, and Res Net for MLP to deal with the too high depth, we should use things like this to deal with the depth in GNN
* the edge attributes is not directly put in the model.

![image-20220807133011648](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807133011648.png)

![image-20220807133035983](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807133035983.png)

![image-20220807135412077](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807135412077.png)

to understand this slides, we should learn the basic knowledge :

![image-20220807135606329](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807135606329.png)

![image-20220807140445519](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807140445519.png)

Next we talk about the formula of GCN:

![image-20220807140537035](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807140537035.png)



![image-20220807140930469](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807140930469.png)

![image-20220807141019833](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807141019833.png)

![image-20220807141048940](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807141048940.png)

Then i write the formulas by hand:

![image-20220807144046722](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807144046722.png)

![image-20220807145257440](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807145257440.png)

the $f_e$ and $f_v$ is the non-linear function

So we did a compromise between not have edge feature at all and have the very explicit vector.

![image-20220807150644533](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807150644533.png)

![image-20220807145904560](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807145904560.png)

The left is simple Attention, the left is the multi-head attention

For simply attention:

![image-20220807150909989](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807150909989.png)

For multi-head attention:

![image-20220807150937781](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807150937781.png)

![image-20220807151705874](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807151705874.png)

![image-20220807152137999](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807152137999.png)





# Practice

## LSTM

I want to finish a seq2seq but it contains  too much and too difficult for me, so I put it a little later. In this, I do a easy text tagging practice:

**Using LSTM to Implement language sentiment dichotomization on IMDB dataset**

![image-20220807002209851](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807002209851.png)

![image-20220807022245908](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220807022245908.png)

## GNN

