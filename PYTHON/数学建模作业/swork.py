import numpy as np
import cvxpy as cp
import pandas as pd
data = pd.read_excel('D:\VSCode\code\PYTHON\数学建模作业\second.xlsx')
data = data.values.T
c = data[:-1, :-1]  # c[i, j]为配送中心i送货到部队用户j的单位运费
d = data[-1, :-1]  # d[j]为部队用户j的需求量
e = data[:-1, -1]  # e[i]为配送中心i的储备量
x = cp.Variable((8, 15), pos=True)  # x[i, j]为配送中心i送货到部队用户j的运量
x1 = cp.Variable((8, 15), pos=True)
y = cp.Variable((8, 15), integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c, x)))
obj1 = cp.Minimize(cp.sum(cp.multiply(c, x1)))
con = [cp.sum(x, axis=0) == d, cp.sum(x, axis=1) <= e,
       x <= 2000 * y, x >= 1000 * y, y >= 0, y <= 1]
con1 = [cp.sum(x1, axis=0) == d, cp.sum(x1, axis=1) <= e, x1 >= 0]
prob = cp.Problem(obj, con)
prob1 = cp.Problem(obj1, con1)
prob.solve(solver='GLPK_MI')
prob1.solve(solver='GLPK_MI')
print('第二种最优值为:', prob.value)
print('第二种最优解为:\n', x.value)
xd = pd.DataFrame(x.value)
xd.to_excel('swork_out1.xlsx')
print('第一种最优解为：', prob1.value)
print('第一种最优解为：', x1.value)
xd = pd.DataFrame(x1.value)
xd.to_excel('swork_out.xlsx')
