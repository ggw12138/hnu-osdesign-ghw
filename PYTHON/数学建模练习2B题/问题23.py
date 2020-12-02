import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_excel('D:\Tencent Files\893398418\养老床位.xlsx')
data = pd.DataFrame(data)
data = data.values

x = data[:, 0]
x = x[0:20]
y = data[:, 1]
y = y[0:20]
y1 = y.copy()
x1 = x.copy()
x = x.reshape(1, -1)
y = y.reshape(1, -1)
x = np.squeeze(x)
y = np.squeeze(y)
x0 = x.copy()
y0 = y.copy()
for i in range(20):
    x[i] = np.log(x[i])  # 对数模型
y = y.reshape(-1, 1)
x = x.reshape(-1, 1)
y1 = y1.reshape(-1, 1)
x1 = x1.reshape(-1, 1)
md = LinearRegression().fit(x, y)
b0 = md.intercept_
bn = md.coef_  # 输出回归系数
R2 = md.score(x, y)  # 计算R^2
# print(b0, bn, R2)
y2 = []
x2 = np.arange(2000, 2025).reshape(1, -1)
for i in range(2000, 2025):
    y2.append(np.squeeze(b0+bn*np.log(i)))
x2 = np.squeeze(x2)
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.title('养老服务床位', fontsize=24)
plt.plot(x2, y2, color='r')  # 预测曲线
plt.plot(x0, y0, color='b')  # 实际曲线
plt.show()

'''data = pd.read_excel('D:\日常应用\学习资料（课堂PPT等等）\数学建模\第二阶段模拟题2\养老服务机构职工人数.xls')
data = pd.DataFrame(data)
data = data.values

x = np.arange(2009, 2014)
X = x.copy()
y1 = data[6, :]
y1 = y1[1:]
y2 = data[7, :]
y2 = y2[1:]
x1 = np.arange(2005, 2025)
x = x.reshape(-1, 1)
y1 = y1.reshape(-1, 1)
y2 = y2.reshape(-1, 1)
y = [y1, y2]
titles = ['城市', '农村']
for i in range(2):
    md = LinearRegression().fit(x, y[i])
    b0 = md.intercept_
    bn = md.coef_  # 输出回归系数
    R2 = md.score(x, y[i])  # 计算R^2
    # print(titles[i])
    #print(b0, bn, R2)
    y1 = []
    for j in range(2005, 2025):
        y1.append(np.squeeze(b0+bn*j))
    plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    plt.title(data[6+i, 0], fontsize=24)
    plt.plot(x1, y1, color='r')  # 预测曲线
    plt.plot(X, y[i], color='b')  # 实际曲线
    plt.show()
'''
