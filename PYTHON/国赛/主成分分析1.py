import numpy as np
from scipy.stats import zscore
import pandas as pd

data1 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\各类数据汇总.xlsx', sheet_name='总收入')
data2 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\各类数据汇总.xlsx', sheet_name='总利润')
data3 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\各类数据汇总.xlsx', sheet_name='每年每季度对应的收入增长率')
data4 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\各类数据汇总.xlsx', sheet_name='每年每季度对应的利润增长率')
data5 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\各类数据汇总.xlsx', sheet_name='供求关系稳定程度')

data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)
data4 = np.array(data4)
data5 = np.array(data5)

for i in range(1, 9):
    data11 = data1[:, i]
    data22 = data2[:, i]
    data33 = data3[:, i]
    data44 = data4[:, i]
    data55 = data5[:, i]
    data11 = data11.reshape(122,1)
    data22 = data22.reshape(122,1)
    data33 = data33.reshape(122,1)
    data44 = data44.reshape(122,1)
    data55 = data55.reshape(122,1)
    opdata1 = np.hstack((data11, data22))
    opdata2 = np.hstack((data33, data44))
    opdata3 = np.hstack((opdata1, opdata2))
    opdata4 = np.hstack((opdata3, data55))

    opdata4 = opdata4.astype(np.float)
    opdata4 -= np.mean(opdata4,axis=0)   # 按列进行标准化
    opdata4 /= np.std(opdata4,axis=0)

    cor = np.corrcoef(opdata4.T)   # 相关系数矩阵
    character_value,character_vector = np.linalg.eig(cor)   # 求特征值和特征向量
    rate = character_value/character_value.sum()    # 计算贡献率

    k = 5  # 提出的主成分个数
    F=character_vector[:,:k]
    score_mat=opdata4.dot(F) #计算主成分得分矩阵
    score1=score_mat.dot(rate[0:k])  # 计算各评价对象的得分

    with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\主成分分析1.1.txt', 'a') as f:
        f.write(str(i))
        f.write('：\n')
        f.write("各评价对象得分：\n")
        f.writelines(str(score1))
        f.write('\n')
    




