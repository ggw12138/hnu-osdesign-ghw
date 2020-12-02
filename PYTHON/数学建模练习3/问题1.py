import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import pylab as pl
from sklearn.linear_model import LinearRegression
from sklearn import svm
import datetime
# 总共可被感染人口
N = 3.24e8   # USA
N1 = 1400050000  # China
N2 = 1324000000  # India
N3 = 10110000  # Swend
# 观察时间
TS = 1.0
# 观察结束时间
ND = 200.0
# 初始易感人数
S0 = N - 1
S1 = N1 - 1
S2 = N2 - 1
S3 = N3 - 1
# 初始感染人数
I0 = 1
INPUT = (S0, I0, 0.0)
INPUT1 = (S1, I0, 0.0)
INPUT2 = (S2, I0, 0.0)
INPUT3 = (S3, I0, 0.0)
gamma = 1/14
beta = 1


def diff_eqs(INP, t):
    Y = np.zeros((3))
    V = INP
    Y[0] = - beta * V[0] * V[1]/N2
    Y[1] = beta * V[0] * V[1]/N2 - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y


t = np.arange(0.0, ND+TS, TS)
# odeint 数值求解微分方程
RES = spi.odeint(diff_eqs, INPUT2, t)
x = RES[:, 1]
x = np.array(x)
x = x.reshape(-1, 1)
x = x[10:25]
pl.subplot(111)
pl.plot(RES[:, 0], '-og', label='Susceptible')
pl.plot(RES[:, 1], '-r', label='Infective')
pl.plot(RES[:, 2], '-k', label='Removal')
pl.legend(loc=0)
pl.title('SIR')
pl.xlabel('Time')
pl.ylabel('Numbers')
pl.xlabel('Time')
pl.show()

#data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\美国疫情数据.xlsx')
#data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\中国疫情数据.xlsx')
#data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\印度疫情数据.xlsx')
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\瑞典疫情数据.xlsx')
order_data = pd.DataFrame(data)
order_data['Date_reported'] = pd.to_datetime(order_data['Date_reported'])
order_data = order_data.set_index('Date_reported')
X = []
Y = []
Y1 = []
beta0 = []
gamma = 1/14

# 比对法选出最合适的时间段
result = []
for j in range(17):
    start = pd.to_datetime('2020-01-31') + datetime.timedelta(days=j*15)
    end = pd.to_datetime('2020-01-31') + datetime.timedelta(days=(j+1)*15)
    test = order_data[start:end]
    test = np.array(test)
    test_cumulative_cases = test[:, 4]
    if test_cumulative_cases.shape[0] < 15:
        break
    else:
        for i in range(test_cumulative_cases.shape[0]-1):
            Y.append(test_cumulative_cases[i])
        Y = np.array(Y)
        Y = Y.reshape(-1, 1)
        md = LinearRegression().fit(x, Y)  # 经典二次线性回归
        b0 = md.intercept_  # 输出第0项系数
        bn = md.coef_  # 输出回归系数
        R2 = md.score(x, Y)  # 计算R^2
        Y = []
        result.append([b0, bn, R2])

#print(result)
# print((pd.to_datetime('2020-01-31')+ datetime.timedelta(days=15)),(pd.to_datetime('2020-01-31')+ datetime.timedelta(days=30)))
# 多项式拟合
x1 = order_data['2020-02-14':'2020-02-29']
y1 = order_data['2020-02-15':'2020-03-01']
y1 = np.array(y1)
x1 = np.array(x1)
y1 = y1[:, 4]
x1 = x1[:, 4]
y1 = y1.reshape(1, -1)
x1 = x1.reshape(1, -1)
x1 = x1.squeeze()
y1 = y1.squeeze()
y1 = y1.astype(np.int)
x1 = x1.astype(np.int)
pfit = np.polyfit(x1, y1, 2)
y_fun = np.poly1d(pfit)
# print(pfit)
print(y_fun)
plt.plot(x1, y1, '*', color='r')
plt.plot(x1, y_fun(x1), color='g')
plt.show()


# 方差求解beta
c = order_data['2020-02-15':'2020-03-01']
c = np.array(c)
cumulative_cases = c[:, 4]
for beta in range(0, 5000):
    a = 0.07+beta*0.0001
    beta0.append(a)
    for i in range(cumulative_cases.shape[0]):
        Y.append((np.exp((a-gamma)*i)-cumulative_cases[i])**2)
    Y = np.array(Y)
    Y1.append(sum(Y))
    Y = []

miny = np.argmin(Y1)
# print(miny)
# print(beta0[miny])

R0 = beta0[miny]*14
print(R0)
