import numpy as np
import matplotlib.pyplot as plt
import pandas as pn
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
# 以下为总确诊人数增长函数，并可根据可接触人数K进行调整模拟
death = 0.03
pd_US = 6.6/14
pd_CN = 7.9/14
pd_IN = 7.97/14
pd_SW = 3.759/14
b_US = pd_US/5        # 可接触人数为k=5,调整K的值可以反应该国家的抗疫隔离措施程度，k越小则防控力度越大
b_CN = pd_CN/10       # k=10
b_IN = pd_IN/9        # k=9
b_SW = pd_SW/3        # k=3
N = 3.24e8   # USA
N1 = 1400050000  # China
N2 = 1324000000  # India
N3 = 10110000  # Swend
pd = [pd_US, pd_CN, pd_IN, pd_SW]
It = [5525217, 90103, 2975701, 86068]   # 治愈率不变，不加以控制
Itk = [5525217, 90103, 2975701, 86068]  # 治愈率不变，加以控制
Itzk = [5525217, 90103, 2975701, 86068]   # 治愈率变，加以控制
Itz = [5525217, 90103, 2975701, 86068]  # 治愈率变，不加以控制
It_nUS = []
It_nCN = []
It_nIN = []
It_nSW = []

It_nUSk = []
It_nCNk = []
It_nINk = []
It_nSWk = []

It_nCNzk = []
It_nUSzk = []
It_nINzk = []
It_nSWzk = []

It_nUSz = []
It_nCNz = []
It_nINz = []
It_nSWz = []
K = [2, 3, 4, 1]


data = pn.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\治愈率预测.xlsx')
data = pn.DataFrame(data)
data = data.values
cn_p = data[:,2]
us_p = data[:,0]
in_p = data[:,1]
sw_p = data[:,3]
probability = [us_p,cn_p,in_p,sw_p]
z = 0
for i in range(75):                          # 预测75天的总感染数,治愈率不变的情况下，分别求出不加以控制和加以控制的增长曲线
    a = (1-death)*It[0]+pd_US*(N-It[0])*It[0]/N-It[0]/14  # 治愈率不变，不加以控制
    b = (1-death)*It[1]+pd_CN*(N1-It[1])*It[1]/N1-It[1]/14
    c = (1-death)*It[2]+pd_IN*(N2-It[2])*It[2]/N2-It[2]/14
    d = (1-death)*It[3]+pd_SW*(N3-It[3])*It[3]/N3-It[3]/14

    e = (1-death)*Itk[0]+K[0]*b_US*(N-Itk[0])*Itk[0]/N-Itk[0]/14  # 治愈率不变，加以控制
    f = (1-death)*Itk[1]+K[1]*b_CN*(N1-Itk[1])*Itk[1]/N1-Itk[1]/14
    g = (1-death)*Itk[2]+K[2]*b_IN*(N2-Itk[2])*Itk[2]/N2-Itk[2]/14
    h = (1-death)*Itk[3]+K[3]*b_SW*(N3-Itk[3])*Itk[3]/N3-Itk[3]/14

    i = (1-death)*Itzk[0]+K[0]*b_US*(N-Itzk[0])*Itzk[0]/N-Itzk[0] * \
        probability[0][z]  # 治愈率变，加以控制
    j = (1-death)*Itzk[1]+K[1]*b_CN*(N1-Itzk[1])*Itzk[1]/N1-Itzk[1]*probability[1][z]
    k = (1-death)*Itzk[2]+K[2]*b_IN*(N2-Itzk[2])*Itzk[2]/N2-Itzk[2]*probability[2][z]
    l = (1-death)*Itzk[3]+K[3]*b_SW*(N3-Itzk[3])*Itzk[3]/N3-Itzk[3]*probability[3][z]

    m = (1-death)*Itz[0]+pd_US*(N-Itz[0])*Itz[0]/N-Itz[0] * \
        probability[0][z]           # 治愈率变，不加以控制
    n = (1-death)*Itz[1]+pd_CN*(N1-Itz[1])*Itz[1]/N1-Itz[1]*probability[1][z]
    o = (1-death)*Itz[2]+pd_IN*(N2-Itz[2])*Itz[2]/N2-Itz[2]*probability[2][z]
    p = (1-death)*Itz[3]+pd_SW*(N3-Itz[3])*Itz[3]/N3-Itz[3]*probability[3][z]
    It[0] = a
    It[1] = b
    It[2] = c
    It[3] = d
    Itk[0] = e
    Itk[1] = f
    Itk[2] = g
    Itk[3] = h
    Itzk[0] = i
    Itzk[1] = j
    Itzk[2] = k
    Itzk[3] = l
    Itz[0] = m
    Itz[1] = n
    Itz[2] = o
    Itz[3] = p
    if i % 5 == 0:
        z += 1
    It_nUS.append(a)
    It_nCN.append(b)
    It_nIN.append(c)
    It_nSW.append(d)
    It_nUSk.append(e)
    It_nCNk.append(f)
    It_nINk.append(g)
    It_nSWk.append(h)
    It_nUSzk.append(i)
    It_nCNzk.append(j)
    It_nINzk.append(k)
    It_nSWzk.append(l)
    It_nUSz.append(m)
    It_nCNz.append(n)
    It_nINz.append(o)
    It_nSWz.append(p)

predata = [It_nUSzk, It_nCNzk, It_nINzk, It_nSWzk]
# 输出文件
pf = pn.DataFrame(list(predata))
# 指定生成的Excel表格名称
file_path = pn.ExcelWriter('D:\VSCode\code\PYTHON\数学建模练习3\总感染人数预测.xlsx')
# 替换空单元格
pf.fillna(' ', inplace=True)
# 输出
pf.to_excel(file_path, encoding='utf-8', index=False)
# 保存表格
file_path.save()


plt.subplot(421)
plt.plot(It_nUS, '-k', label='US(k1=5),unchange')
plt.plot(It_nUSk, '-r', label='US(k2=2),unchange')
plt.legend(loc = 'upper right')

plt.subplot(422)
plt.plot(It_nCN, '-k', label='CN(k1=10),unchange')
plt.plot(It_nCNk, '-r', label='CN(k2=3),unchange')
plt.legend(loc = 'upper right')

plt.subplot(423)
plt.plot(It_nIN, '-k', label='IN(k1=10),unchange')
plt.plot(It_nINk, '-r', label='IN(k2=4),unchange')
plt.legend(loc = 'upper right')

plt.subplot(424)
plt.plot(It_nSW, '-g', label='SW(k1=3),unchange')
plt.plot(It_nSWk, '-r',label='SW(k2=1),unchange')
plt.legend(loc = 'upper right')

plt.subplot(425)
plt.plot(It_nUSzk, '-g', label='US(k1=2),change')
plt.plot(It_nUSz,'-y',label='US(K2=5),change')
plt.legend(loc = 'upper right')

plt.subplot(426)
plt.plot(It_nCNzk, '-g', label='CN(k1=3),change')
plt.plot(It_nCNz,'-y',label='CN(K2=10),change')
plt.legend(loc = 'upper right')

plt.subplot(427)
plt.plot(It_nINzk, '-g', label='IN(k1=4),change')
plt.plot(It_nINz,'-y',label='IN(K2=10),change')
plt.legend(loc = 'upper right')

plt.subplot(428)
plt.plot(It_nSWzk, '-g', label='SW(k1=1),change')
plt.plot(It_nSWz,'-y',label='SW(K2=3),change')
plt.legend(loc = 'upper right')

plt.show()

'''data = pn.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\美国治愈人数数据.xlsx')
#data = pn.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\印度治愈人数数据.xlsx')
#data = pn.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\中国治愈人数数据.xlsx')
#data = pn.read_excel('D:\VSCode\code\PYTHON\数学建模练习3\瑞典治愈人数数据.xlsx')
data = pn.DataFrame(data)
data = data.values
y = data[:, 1]
num = y.shape[0]
y = y.reshape(1, -1)
x = np.arange(0, 40)
x = x.reshape(1, -1)
x = x.astype(np.float32)
y = y.astype(np.float32)
x = x.squeeze()
y = y.squeeze()

def Y(X, a, t, c): return a*np.exp(-1*X/t)+c     #回归模型印度适用
def Y1(X, a, t, c): return a+t*np.exp(-c*X)      #回归模型美国
def Y2(X, a, t, c): return t+(a-t)/(1+np.exp)    #中国和瑞典适用

popt, pcov = curve_fit(Y1, x, y,maxfev=5000)     #迭代5000次
print('popt: ', popt)
a, t, c = popt
y_pre = a+t*np.exp(-c*x)
plt.plot(x, y, 'ko', label="Original Data")
plt.plot(x, y_pre, 'r-', label="Fitting Curve")
plt.legend()
plt.show()
print(r2_score(y, y_pre))

x1 = np.arange(40,55)
y_predict = a+t*np.exp(-c*x1) 
plt.plot(x1, y_predict,'g-',label='prediction data')
plt.legend()
plt.show()
print(y_predict)

'''