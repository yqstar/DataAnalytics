# -*- coding:utf-8 -*-

import os
import time

# 三大件
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# os.sep,可根据所处的平台，自动采用相应的分隔符号
# "sep".join(seq),连接字符串数组。将字符串、元组、列表中的元素以指定的字符（分隔符）连接生成一个新的字符串
# os.path.join()，将多个路径组合返回
path = 'data' + os.sep + 'data.txt'

# pd_data = pd.read_csv(path, header=None, names=["Exam1", "Exam2", "Admitted"]).as_matrix()
pd_data = pd.read_csv(path, header=None, names=["Exam1", "Exam2", "Admitted"]).as_matrix()
cols = pd_data.shape[1]

X = pd_data[:, 0:cols-1]
X = np.insert(X, 0, np.ones(len(X)), axis=1)
y = pd_data[:, cols-1:cols]


# sigmoid函数

# sigmoid : 映射到概率的函数
def sigmoid(x):
    return 1/(1+np.exp(x))


# model : 返回预测结果值
def model(X, theta):
    # numpy.insert(arr, obj, value, axis=None)
    # arr: 为目标向量
    # obj: 为目标位置
    # value: 为想要插入的数值
    # axis: 为插入的维度，axis=1表示对于列操作，axis=0表示行操作
    # 在X的左侧加一列数据1
    # X = np.insert(X, 0, np.ones(len(X)), axis=1)
    # np.dot(a,b)返回a,b的内积
    # np.multiply(a,b)返回a,b对应元素相乘结果
    return sigmoid(np.dot(X, theta.T))


# 初始化theta
theta = np.zeros([1, 3])

tf = model(X, theta)


# cost : 根据参数计算损失
def cost(X, y, theta):

    # X = np.insert(X, 0, np.ones(len(X)), axis=1)

    left = np.multiply(y, np.log(model(X, theta)))

    right = np.multiply(1-y, np.log(1-model(X, theta)))

    return -np.sum(left+right)/len(X)

# print(cost(X ,y, theta))


# gradient : 计算每个参数的梯度方向
def gradient(X, y, theta):

    grad = np.zeros(theta.shape[1])

    error = model(X, theta)-y

    for j in range(grad.shape[0]):

        grad[j] = np.sum(np.multiply(X[:, j], error.T))/len(X)

    return grad


print(gradient(X, y, theta))

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2

def stopCriterion(type, value, threshold):
    #设定三种不同的停止策略
    if type == STOP_ITER:
        return value > threshold
    elif type == STOP_COST:
        return abs(value[-1]-value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold

def shuffle_data(data):

    np.random.shuffle(data)
    
    cols = data.shape[1]
    X = data[:, 0:cols-1]
    y = data[:, cols-1:]
    return X, y


# descent : 进行参数更新
def descent(data, theta, batchSize, stopType, thresh, alpha):
    # 梯度下降求解

    init_time = time.time()
    i = 0  # 迭代次数
    k = 0  # batch
    X, y = shuffle_data(data)
    grad = np.zeros(theta.shape)  # 计算的梯度
    costs = [cost(X, y, theta)]  # 损失值

    while True:
        grad = gradient(X[k:k + batchSize], y[k:k + batchSize], theta)
        k += batchSize  # 取batch数量个数据
        if k >= n:
            k = 0
            X, y = shuffle_data(data)  # 重新洗牌
        theta = theta - alpha * grad  # 参数更新
        costs.append(cost(X, y, theta))  # 计算新的损失
        i += 1

        if stopType == STOP_ITER:
            value = i
        elif stopType == STOP_COST:
            value = costs
        elif stopType == STOP_GRAD:
            value = grad
        if stopCriterion(stopType, value, thresh): break

    return theta, i - 1, costs, grad, time.time() - init_time



# accuracy: 计算精度
