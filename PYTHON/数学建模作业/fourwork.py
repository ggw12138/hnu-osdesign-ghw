import numpy as np
import networkx as nx
import pylab as plt
import pandas as pd
import matplotlib.pyplot as pltt

data = pd.read_excel(r"D:\VSCode\code\PYTHON\数学建模作业\data6.xlsx", header=None)
D = list(data[1:96][0])  # 顶点
x = list(data[1:96][1])  # 顶点坐标
y = list(data[1:96][2])
lb = list(data[1:96][3])  # 顶点类别
lj1 = list(data[1:96][4])  # 连接的点
lj2 = list(data[1:96][5])
lj3 = list(data[1:96][6])
a = np.zeros((95, 95))  # 顶点之间有边相连记为1，无为0
for i in range(95):
    for j in range(95):
        if lj1[i] == D[j]:
            a[i, j] = 1
        if lj2[i] == D[j]:
            a[i, j] = 1
        if lj3[i] == D[j]:
            a[i, j] = 1

# 画出顶点，紫色——第一类别点，蓝色——第二类别点，红色——点三类别点
plt.title("Undirected Graph")
for i in range(95):
    if lb[i] == 1:
        pltt.plot(x[i], y[i], 'm*')
    elif lb[i] == 2:
        pltt.plot(x[i], y[i], 'bx')
    else:
        pltt.plot(x[i], y[i], 'r.')
    pltt.annotate(str(D[i]), xy=(x[i], y[i]))
# 将有连接的点用黄色线连接
for i in range(95):
    for j in range(95):
        if a[i, j] == 1:
            xx = [x[i], x[j]]
            yy = [y[i], y[j]]
            pltt.plot(xx, yy, 'y')
plt.xlabel("x")
plt.ylabel("y")
pltt.show()


# 设置权重
w = np.zeros((95, 95))
for i in range(95):
    for j in range(95):
        if a[i, j] == 1:
            w[i, j] = ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
        elif i == j:
            w[i, j] = 0
        else:
            w[i, j] = float("inf")
for i in range(95):
    for j in range(i):
        w[i, j] = w[j, i]


# 画最小生成树
L = []  # 设置权序列
for i in range(95):
    for j in range(95):
        if a[i, j] == 1:
            L.append((i, j, w[i, j]))
map = dict(zip(range(95), D))
# 得到最小生成树
G = nx.Graph()
G.add_weighted_edges_from(L)
T = nx.minimum_spanning_tree(G)  # 返回可迭代对象
mst = nx.minimum_spanning_edges(G, data=False)
edgelist = list(mst)  # 最小生成树连接的点
edgelist = sorted(edgelist)
# 画图
plt.title("minimum spanning tree")
for i in range(95):
    if lb[i] == 1:
        pltt.plot(x[i], y[i], 'm*')
    elif lb[i] == 2:
        pltt.plot(x[i], y[i], 'bx')
    else:
        pltt.plot(x[i], y[i], 'r.')
    pltt.annotate(str(D[i]), xy=(x[i], y[i]))
# 将最小生成树连接的点用黄色线连接
for i in range(len(edgelist)):
    tx = [x[edgelist[i][0]], x[edgelist[i][1]]]
    ty = [y[edgelist[i][0]], y[edgelist[i][1]]]
    pltt.plot(tx, ty, 'y')
plt.xlabel("x")
plt.ylabel("y")
pltt.show()


# 计算L到R3最短路径和距离
G3 = nx.Graph(w)  # 构造赋权有向图
G3 = nx.relabel_nodes(G3, map)  # 修改顶点编号
p = nx.shortest_path(G3, source='L', target='R3', weight='weight')
d = nx.shortest_path_length(G3, source='L', target='R3', weight='weight')
print('path=', p)
print('d=', d)
# 画最短路径图
plt.title("L to R3 Shortest path")
for i in range(95):
    if lb[i] == 1:
        pltt.plot(x[i], y[i], 'm*')
    elif lb[i] == 2:
        pltt.plot(x[i], y[i], 'bx')
    else:
        pltt.plot(x[i], y[i], 'r.')
    pltt.annotate(str(D[i]), xy=(x[i], y[i]))
n = []
for i in range(len(p)):
    for j in range(95):
        if p[i] == D[j]:
            n.append(j)
px = []
py = []  # 记录经过点的坐标
for i in range(len(p)):
    px.append(x[n[i]])
    py.append(y[n[i]])
pltt.plot(px, py, 'y')
plt.xlabel("x")
plt.ylabel("y")
pltt.show()
