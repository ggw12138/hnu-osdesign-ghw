import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_excel('D:\日常应用\学习资料（课堂PPT等等）\数学建模\第二阶段模拟题2\年度数据.xls')
data = pd.DataFrame(data)
data = data.values
#   以下处理前11行的数据
x = np.arange(2000, 2020).reshape(1, 20)   # 20年的年份数组
x = np.squeeze(x)    # 数据处理，降维
x1 = np.arange(2000, 2025).reshape(1, 25)
x1 = np.squeeze(x1)
for j in range(data.shape[0]-4):  # 读取前20行的数据处理
    y = data[j]
    y = y[1:]
    y = y.reshape(1, 20)
    y = np.squeeze(y)
    X = []
    Y = []
    for i in range(20):
        X.append(x[i])  # 线性回归模型   y = a + bx
        Y.append(y[i])
    X = np.array(X)
    Y = np.array(Y)
    Y1 = Y.copy()
    X = X.reshape(-1, 1)  # 变化为一元一次线性回归
    Y = Y.reshape(-1, 1)
    md = LinearRegression().fit(X, Y)  # 经典二次线性回归
    b0 = md.intercept_  # 输出第0项系数
    bn = md.coef_  # 输出回归系数
    R2 = md.score(X, Y)  # 计算R^2
    #print(data[j, 0])
    #print(b0, bn, R2)
    y1 = []
    for i in range(2000, 2025):  # 打印2020到2024年的预测结果
        y1.append(np.squeeze(b0+bn*i))

    plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    plt.title(data[j, 0], fontsize=24)
    plt.plot(x1, y1, color='r')  # 预测曲线
    plt.plot(X, Y, color='b')  # 实际曲线
    plt.show()

#   以下处理年龄65+人口数据
#   以下处理消费水平数据
for j in range(data.shape[0]-4, data.shape[0]):  # 居民消费水平
    y = data[j]
    y = y[1:]
    y = y.reshape(1, 20)
    y = np.squeeze(y)
    Y = []
    X = x
    for i in range(20):
        Y.append(np.log(y[i]))
    X = np.array(X)
    Y = np.array(Y)
    X = X.reshape(-1, 1)
    Y = Y.reshape(-1, 1)
    md = LinearRegression().fit(X, Y)
    b0 = md.intercept_
    bn = md.coef_  # 输出回归系数
    R2 = md.score(X, Y)  # 计算R^2
    y1 = []
    for i in range(2000, 2025):  # 打印2020到2024年的预测结果
        y1.append(np.squeeze(np.exp(b0+bn*i)))
        print(b0, bn, R2)
        print(i, np.squeeze(np.exp(b0+bn*i)))
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.title(data[j, 0], fontsize=24)
    plt.plot(x1, y1, color='r')  # 预测曲线
    plt.plot(X, y, color='b')  # 实际曲线
    plt.show()
