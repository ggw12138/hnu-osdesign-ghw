from sklearn.cross_decomposition import PLSRegression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模B题\问题一元旦.xlsx')
data = data.values
y = np.array(data[:, 1])
x = np.array(data[:,2:5])
x -= np.mean(x, axis=0)
x /= np.std(x, axis=0)
y -= np.mean(y, axis=0)
y /= np.std(y, axis=0)
# 经典最小二乘回归
md = LinearRegression().fit(x, y)
b0 = md.intercept_
bn = md.coef_  # 输出回归系数
R2 = md.score(x, y)  # 计算R^2
print("以下是经典最小二乘回归————————")
print("b0=%.4f" % (b0))
print("bn=",bn)
print("\n拟合优度R^2=",R2)

pls = PLSRegression(n_components=3)
pls.fit(x, y)
print("以下是偏最小二乘回归——————————")
print("\nb0=", pls.y_mean_)
print("\n回归系数bn=\n", pls.coef_)
print("\n拟合优度R^2\n", pls.score(x, y))
