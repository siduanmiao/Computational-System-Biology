# Vedio

Convolutional neural network inside our brain

![image-20220804134104213](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804134104213.png)

![image-20220804142050663](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804142050663.png)

ResNet:

>Let us back to the origin of deep learning, compared with the traditional machine learning, the key feature of deep learning lies in the network layer deeper and nonlinear transformation (activated), automatic feature extraction and feature transformation, among them, the nonlinear transformation is the key target, it will be the data mapping to achieve the space in order to better complete the "data classification". With the continuous increase of network depth, more and more activation functions are introduced, and the data are mapped to a more discrete space. At this time, it is difficult to return the data to the origin (identity transformation). In other words, **the amount of computation required for the neural network to map the data back to the origin is far more than we can afford**.
>
>The design intuition of ResNet is: Deeper network model should not compare the performance effect of shallow network model to the performance effect of poor, but in fact it is based on the network depth deepening is accomplished by linear mapping of identity, but we are possible because of the activation function of network, so basically is a nonlinear mapping, in this case, it is difficult to have identity mapping. Therefore, **the original intention of Residual Learning was to make the internal structure of the model have at least the ability of identity mapping**. To ensure that in the process of stacking the network, at least the network will not be degraded because of continuing to stack!

Resnet provides two options, namely, **identity mapping** and **residual mapping**. If the network has reached the optimum and the residual mapping is deepened, the residual mapping will be pushed to 0, leaving only identity mapping. In this way, the network is always in the optimal state in theory, and the performance of the network will not decrease with the increase of depth.

![image-20220804150532487](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804150532487.png)

![image-20220804155118978](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804155118978.png)

The $F(x)$ is used to approximate the residue function $H(x)-x$, the all layers of a neutral network is used to approximate a function.

![image-20220804153118686](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804153118686.png)

to ensure the complicated model can contain the simple model.

![image-20220804154933746](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804154933746.png)

![image-20220804155706273](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804155706273.png)

![image-20220804163918410](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804163918410.png)

![image-20220804190107384](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804190107384.png)

![image-20220804190211973](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804190211973.png)

![image-20220804190514170](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804190514170.png)

two important feature of CNN: Local awareness and parameter sharing

 every filters have a set of sharing parameters:

![image-20220804192141921](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804192141921.png)

we have 3 groups of parameters.

![image-20220804192307438](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804192307438.png)

There are many hard-code filters in the past 30 years, but different images have different suitable features, we should learn from data.

![image-20220804194040710](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804194040710.png)

![image-20220804194801124](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804194801124.png)

After the all convolutional layer, we captured the features,then we get into the fully-connected NN.

![image-20220804195140804](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804195140804.png)

padding: You want each input square to be the center of the convolution window

![在这里插入图片描述](Lecture%203%20Convolutional%20Neural%20Networks.assets/20200825171851456.gif)

Stride: We want to reduce the number of input parameters and reduce the computation

![image-20220804195957619](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804195957619.png)

Dilated convolutions:

![image-20220804195921014](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804195921014.png)

Number of channels in the convolutional kernel of a CNN = Number of channels in the convolutional input layer

Number of channels (depth) in the convolutional output layer of the CNN = Number of convolutional kernels

![image-20220804205352245](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804205352245.png)

**Data augmentation** techniques are usually used in **deep learning based object detection**. Data augmentation enables the generation of a large group of training samples to improve robustness of the detector,. Yet, it is seldom used in visual tracking. The work in is the first to exploit the data augmentation in CNN based visual tracking.

![image-20220804204207696](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804204207696.png)

![image-20220804204435892](Lecture%203%20Convolutional%20Neural%20Networks.assets/image-20220804204435892.png)