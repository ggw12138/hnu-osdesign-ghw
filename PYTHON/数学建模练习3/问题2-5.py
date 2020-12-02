import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\总感染人数预测.xlsx')
data = pd.DataFrame(data)
data = data.values

CN = [-1990.3933, 78229.502, 10.5011, 2.00717]
IN = [3334.53074, -7.18682, -25540.57478]
SW = [221.83039, 4979.40897, 14.38473, 0.47989]

def Y(A1, A2, x0, dx, x):
    return A2+(A1-A2)/(1+np.exp((x-x0)/dx))


def Y1(A1, t1, y0, x):
    return A1*np.exp(-1*x/t1)+y0

x = np.arange(40, 55)
CN_pre = Y(CN[0], CN[1], CN[2], CN[3], x)
IN_pre = Y1(IN[0], IN[1], IN[2], x)
SW_pre = Y(SW[0], SW[1], SW[2], SW[3], x)

plt.plot(CN_pre,'r',label='CN_pre')
plt.plot(SW_pre,'k',label='SW_pre')
plt.plot(IN_pre,'b',label='IN_pre')
plt.legend()
plt.show()

#data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\美国治愈人数及累计确诊人数数据.xlsx')
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\印度治愈人数数据及累计确诊人数.xlsx')
data = pd.DataFrame(data)
data = data.values
y = data[:, 3]
x = np.arange(y.shape[0])
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
#美国和印度治愈率预测
md = LinearRegression().fit(x, y)
b0 = md.intercept_  # 输出第0项系数
bn = md.coef_  # 输出回归系数
R2 = md.score(x, y)  # 计算R^2
print("b0=",b0,"bn=", bn,"R2=", R2)
X = np.arange(y.shape[0], y.shape[0]+15)
X = X.reshape(-1, 1)
print("预测值：",md.predict(X))

#中国的治愈率预测
x_cn = np.arange(55,70)
CN_parmas = [0.02645,0.91615,10.37248,1.75078]
def Y(A1, A2, x0, dx, x):
    return A2+(A1-A2)/(1+np.exp((x-x0)/dx))
CN_pred = Y(CN_parmas[0], CN_parmas[1],CN_parmas[2],CN_parmas[3], x_cn)
print(CN_pred)

data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\治愈率预测.xlsx')
data = pd.DataFrame(data)
data = data.values
cn_p = data[:, 2]
us_p = data[:, 0]
in_p = data[:, 1]
sw_p = data[:, 3]
probability = [us_p, cn_p, in_p, sw_p]
print(probability[0][0])
