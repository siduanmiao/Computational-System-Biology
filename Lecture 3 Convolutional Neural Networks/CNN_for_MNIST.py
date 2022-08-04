# -*- coding:utf-8 -*-
# 作者：司端淼
# 创建：2022-08-05
# 内容：MIT课程第三节课CNN内容后，尝试在手写数据集MNIST上构建经典的LeNet-5模型进行训练

import torch
from torch import nn
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset,DataLoader
from torch.utils.tensorboard import SummaryWriter
import numpy as np

print(torch.cuda.is_available())
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 官网上给的最优的读取数据方式
train_dataset = torchvision.datasets.MNIST('data/',download=True,train=True,
                               transform=transforms.Compose([
                                   transforms.ToTensor(),
                                  transforms.Normalize((0.1307,), (0.3081,)),
                               ]))
test_dataset = torchvision.datasets.MNIST('data/',download=True,
                              transform=transforms.Compose([
                                  transforms.ToTensor(),
                                  transforms.Normalize((0.1307,), (0.3081,)),
                              ]))
# 搭建模型
class LeNet(nn.Module):
    def __init__(self):
        #使用nn.Module的初始化
        super(LeNet,self).__init__()
        # 模型按照文献的样式搭建
        self.model = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, padding=2),
            nn.MaxPool2d(2),
            nn.ReLU(inplace=True),
            nn.Conv2d(6, 16, kernel_size=5),
            nn.MaxPool2d(2),
            nn.ReLU(inplace=True),
            nn.Conv2d(16, 120, kernel_size=5),
            nn.ReLU(inplace=True),
            # 到这里已经展平了
            nn.Flatten(),#这里必须要展平而不能直接链接线性层，原因暂时不详，可能是表示形式的问题
            nn.Linear(120, 84),
            nn.ReLU(inplace=True),
            nn.Linear(84, 10),
            nn.ReLU(inplace=True),
            nn.LogSoftmax()
        )

    def forward(self,input):
        input = self.model(input)
        return input

# 按照批次读入的Dataloder
train_dataloader=DataLoader(train_dataset,batch_size=64,shuffle=True)
test_dataloader=DataLoader(test_dataset,batch_size=64,shuffle=True)
len_train=len(train_dataset)
len_test=len(test_dataset)
# 创建模型
model=LeNet().to(device)
# 定义损失函数和优化器
loss_function = torch.nn.NLLLoss().to(device)
optimizer = torch.optim.SGD(
    model.parameters(),#优化器将模型的参数纳入
    lr=0.001,
    momentum=0.9
)
# 监视器
writer=SummaryWriter("result")

# 模型训练
epoch=20
total_train_step=0
total_test_step=0
for epoch in range(epoch):
    total_accuracy=0
    model.train()
    # train
    for data in train_dataloader:
        imgs, target = data
        imgs = imgs.to(device)  # GPU
        target = target.to(device)  # GPU
        output=model(imgs)
        result_loss = loss_function(output, target)
        optimizer.zero_grad()  # 将所有的参数设为零，因为pytorch中梯度的值可以累加
        result_loss.backward()  # 计算所得到的参数
        optimizer.step()  # 对模型中的参数进行调节
        accuracy = (output.argmax(1) == target).float().sum()
        total_accuracy = total_accuracy + accuracy
        total_train_step = total_train_step + 1
        if total_train_step % 100 == 0:
            writer.add_scalar("train_loss", result_loss, total_train_step)
        # 这里看的是当前这一步的loss
    writer.add_scalar("train_acc", total_accuracy / len_train, epoch)
    # test
    total_accuracy = 0
    model.eval()
    with torch.no_grad():
        for data in test_dataloader:
            imgs, target = data
            imgs = imgs.to(device)  # GPU
            target = target.to(device)  # GPU
            output = model(imgs)
            result_loss = loss_function(output, target)
            accuracy = (output.argmax(1) == target).float().sum()
            total_accuracy = total_accuracy + accuracy
            total_test_step=total_test_step+1
            if total_test_step % 100 == 0:
                writer.add_scalar("train_loss", result_loss, total_test_step)
        writer.add_scalar("test_acc", total_accuracy / len_test, epoch)
writer.close()