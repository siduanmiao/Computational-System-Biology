# Vedio

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

==we can use RNN and so on as a encoder and decoder!!==

Like seq2seq:

![image-20220806181022430](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806181022430.png)

![image-20220806181105123](Lecture%204%20Recurrent%20Neural%20Networks,%20Graph%20Neural%20Networks.assets/image-20220806181105123.png)



