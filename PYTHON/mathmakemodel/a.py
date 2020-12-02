import pandas as pd
import xlrd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
io=r'D:\VSCode\code\PYTHON\mathmakemodel\汽车产业相关数据.xlsx'
io1=r'D:\VSCode\code\PYTHON\mathmakemodel\数据.txt'
df1=pd.read_excel(io)
datas=df1
'''
data = xlrd.open_workbook(io)
table = data.sheets()[0]
start=2
end=8
nrows=table.nrows #row
ncols=table.ncols #col

print(nrows)
print(ncols)

df=pd.DataFrame(df1)
print(df)

#print("输出列标题",df.columns.values)
#print("获取到所有的值:\n{0}".format(df))#格式化输出



'''

'''
#txt文本输入，kmeans聚类
def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retName = []
    retData = []
    for line in lines:
        items = line.strip().split(',')
        retName.append(items[0])                    #插入名字
        retData.append([float(items[i]) for i in range(1,len(items))])   #插入剩余数据
    return retName, retData

if __name__ == '__main__':
    Name, Data = loadData(io1)
    
    clusters_cnt = 3
    km = KMeans(n_clusters=clusters_cnt,init='k-means++')
    label = km.fit_predict(Data)
 
    outputName = []
    for i in range(clusters_cnt):
        outputName.append([])
    for i in range(len(Name)):
        outputName[label[i]].append(Name[i])
    print(outputName)
    print(km.labels_)   #标签,每个样本集对应的类别
    print(km.cluster_centers_)  #聚类质心
'''

'''
暂时未通过代码
#聚点可视化
def getXY(dataSet):
    import numpy as np
    m = shape(dataSet)[0]  # 数据集的行
    X = []
    Y = []
    for i in range(m):
        X.append(dataSet[i,0])
        Y.append(dataSet[i,1])
    return np.array(X), np.array(Y)
 
# 数据可视化
def showCluster(dataSet, k, clusterAssment, centroids):
    fig = plt.figure()
    plt.title("K-means")
    ax = fig.add_subplot(111)
    data = []
 
    for cent in range(k): #提取出每个簇的数据
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] #获得属于cent簇的数据
        data.append(ptsInClust)
 
    for cent, c, marker in zip( range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's'] ): #画出数据点散点图
        X, Y = getXY(data[cent])
        ax.scatter(X, Y, s=80, c=c, marker=marker)
 
    centroidsX, centroidsY = getXY(centroids)
    ax.scatter(centroidsX, centroidsY, s=1000, c='black', marker='+', alpha=1)  # 画出质心点
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.show()
''' 


'''#建立图表
    plt.figure()
    new_ticks = np.linspace(0, 8, 9)
    plt.xticks(new_ticks)
    plt.yticks(new_ticks)
    plt.show()
'''
'''
    #获取Kmeans聚类结果每一类的数据
    res0=pd.DataFrame(km.labels_==0) 
    res1=pd.DataFrame(km.labels_==1)
    res2=pd.DataFrame(km.labels_==2)

    print(res0)
    print(res1)
    print(res2)
    #centroids, clusterAssment = KMeans(data, cluster_Num)
    #showCluster(Data, clusters_cnt, clusterAssment, centroids)
'''

import numpy.linalg as nlg
import warnings
warnings.filterwarnings("ignore")
'''
#因子分析1
data=pd.DataFrame(df1)
data.columns=["总资产 ","总产值 ","专利数","总产量 ","总利润 ","总销量 ","占有率 ","财政政策"]
data.index=['北京','天津','吉林','上海','江苏','浙江','湖北']
#数据标准化
data=(data-data.mean())/data.std()
data1=data.copy()
#相关矩阵C
C=data.corr()
#计算特征值和特征向量
eig_value,eig_vector=nlg.eig(C) #计算特征值和特征向量
eig=pd.DataFrame() #利用变量名和特征值建立一个数据框
eig['names']=data.columns#列名
eig['eig_value']=eig_value#特征值

#确定公因子个数k
from math import sqrt
for k in range(1,11): #确定公共因子个数
    if eig['eig_value'][:k].sum()/eig['eig_value'].sum()>=0.8: #如果解释度达到80%, 结束循环
        print(k)
        break

#print(eig['eig_value'][:2].sum()/eig['eig_value'].sum())
#构造初始因子载荷矩阵A
col0=list(sqrt(eig_value[0])*eig_vector[:,0]) #因子载荷矩阵第1列
col1=list(sqrt(eig_value[1])*eig_vector[:,1]) #因子载荷矩阵第2列
A=pd.DataFrame([col0,col1]).T #构造因子载荷矩阵A
A.columns=['factor1','factor2'] #因子载荷矩阵A的公共因子

#建立因子模型
h=np.zeros(8) #变量共同度，反映变量对共同因子的依赖程度，越接近1，说明公共因子解释程度越高，因子分析效果越好
D=np.mat(np.eye(8))#特殊因子方差，因子的方差贡献度 ，反映公共因子对变量的贡献，衡量公共因子的相对重要性
A=np.mat(A) #将因子载荷阵A矩阵化
for i in range(8):
    a=A[i,:]*A[i,:].T #行平方和
    h[i]=a[0,0]  #计算变量X共同度,描述全部公共因子F对变量X_i的总方差所做的贡献，及变量X_i方差中能够被全体因子解释的部分
    D[i,i]=1-a[0,0] #因为自变量矩阵已经标准化后的方差为1，即Var(X_i)=第i个共同度h_i + 第i个特殊因子方差


from numpy import eye, asarray, dot, sum, diag #导入eye,asarray,dot,sum,diag 函数
from numpy.linalg import svd #导入奇异值分解函数

#将因子表示成变量的线性组合
def varimax(Phi, gamma = 1.0, q =8, tol = 1e-6): #定义方差最大旋转函数
    p,k = Phi.shape #给出矩阵Phi的总行数，总列数
    R = eye(k) #给定一个k*k的单位矩阵
    d=0
    for i in range(q):
        d_old = d
        Lambda = dot(Phi, R)#矩阵乘法
        u,s,vh = svd(dot(Phi.T,asarray(Lambda)**3 - (gamma/p) * dot(Lambda, diag(diag(dot(Lambda.T,Lambda)))))) #奇异值分解svd
        R = dot(u,vh)#构造正交矩阵R
        d = sum(s)#奇异值求和
    if d_old!=0 and d/d_old:
        return dot(Phi, R)#返回旋转矩阵Phi*R

rotation_mat=varimax(A)#调用方差最大旋转函数
rotation_mat=pd.DataFrame(rotation_mat)#数据框化

#计算因子得分
data=np.mat(data) #矩阵化处理
factor_score=(data).dot(A) #计算因子得分
factor_score=pd.DataFrame(factor_score)#数据框化
factor_score.columns=['因子A','因子B'] #对因子变量进行命名
print(factor_score)

from factor_analyzer import FactorAnalyzer
fa = FactorAnalyzer(n_factors=2,method='principal')
fa.loadings_ = C
print("\n成分矩阵:\n", fa.loadings_)#成分矩阵
#print("\n公因子方差:\n",fa.get_communalities())
var = fa.get_factor_variance()  # 给出贡献率
#print("\n解释的总方差（即贡献率）:\n", var)
fa_15_df = pd.DataFrame({'特征值': var[0], '方差贡献率': var[1], '方差累计贡献率': var[2]})
print("\n",fa_15_df)

#将各因子乘上他们的贡献率除以总的贡献率,得到因子得分中间值
b = (factor_score*var[1])/var[2]
#将各因子得分中间值相加，得到综合得分
b['score'] = b.apply(lambda x: x.sum(), axis=1)
print(b)
'''

from factor_analyzer import Rotator
from factor_analyzer import FactorAnalyzer
from math import sqrt
fa = FactorAnalyzer(11, rotation=None)
fa.fit(datas)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
plt.scatter(range(1, datas.shape[1]+1), ev)
plt.plot(range(1, datas.shape[1]+1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

fa = FactorAnalyzer(n_factors=2, method='principal', rotation='varimax')
fa.fit(datas)
# 公因子方差
print(fa.get_communalities())
# 特征值
print("\n特征值:\n", fa.get_factor_variance()[0])
# 方差贡献率
print("\n方差贡献率:\n", fa.get_factor_variance()[1])
# 累积方差贡献率
print("\n累计方差贡献率:\n", fa.get_factor_variance()[2])

print("\n成分矩阵：\n", fa.loadings_)
rotator = Rotator()
load_matrix = rotator.fit_transform(fa.loadings_)
print(load_matrix)

# 因子得分系数矩阵
# 相关系数
corr = datas.corr()
# array转matrix
corr = np.mat(corr)

# 因子载荷矩阵
load_matrix = np.mat(load_matrix)
pr_matrix_score = np.dot(nlg.inv(corr), load_matrix)
print(pr_matrix_score)



eig_value,eig_vector=nlg.eig(corr) #计算特征值和特征向量
eig=pd.DataFrame() #利用变量名和特征值建立一个数据框
eig['names']=datas.columns#列名
eig['eig_value']=eig_value#特征值
col0=list(sqrt(eig_value[0])*eig_vector[:,0]) #因子载荷矩阵第1列
col1=list(sqrt(eig_value[1])*eig_vector[:,1]) #因子载荷矩阵第2列
A=pd.DataFrame([col0,col1]).T #构造因子载荷矩阵A
print(A)

# 各因子得分
factor_score = pd.DataFrame(np.dot(np.mat(datas), np.mat(A)))
factor_score.columns = ['F1','F2']
factor_score.index = datas.index
print(factor_score)
# 综合得分
# 各因子方差贡献率
cnt_var = [[0.65278715,0.23489924]]
factor_score['score'] = np.dot(np.mat(factor_score), cnt_var) / 0.82979849
# 按照综合得分降序
factor_score.sort_values(by='score', ascending=False, inplace=True)
print(factor_score)

