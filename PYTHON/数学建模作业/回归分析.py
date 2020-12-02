from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模作业\粮食数据1.xlsx')
data = data.values
y = np.array(data[:, 1])
x = np.array(data[:, 2:])
# 经典最小二乘回归
md = LinearRegression().fit(x, y)
b0 = md.intercept_
bn = md.coef_  # 输出回归系数
R2 = md.score(x, y)  # 计算R^2
print("以下是经典最小二乘回归————————\n\n")
print("b0=%.4f\nbn=" % (b0))
print(bn)
print("\n拟合优度R^2=%.4f" % R2)

# 偏最小二乘回归
pls = PLSRegression(n_components=2)
pls.fit(x, y)
print("以下是偏最小二乘回归——————————\n\n")
print("\n回归系数bn=\n", pls.coef_)
print("\n拟合优度\n", pls.score(x, y))

# 主成分回归
pca = PCA(n_components=4)
newX = pca.fit_transform(x)
print("以下是主成分回归——————————————\n\n")
print(pca.explained_variance_ratio_)
lr = LinearRegression().fit(newX, y)
print("\nb0=", lr.intercept_)
print("\n回归系数", lr.coef_)
print("\n拟合优度", lr.score(newX, y))
