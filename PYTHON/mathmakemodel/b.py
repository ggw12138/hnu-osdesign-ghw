import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import copy 
import re
import xlrd
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn import metrics,datasets,manifold
np.seterr(divide='ignore', invalid='ignore')
#极小型指标 -> 极大型指标
def dataDirection_1(datas):         
        return np.max(datas)-datas     #套公式

#中间型指标 -> 极大型指标
def dataDirection_2(datas, x_best):
    temp_datas = datas - x_best
    M = np.max(abs(temp_datas))
    answer_datas = 1 - abs(datas - x_best) / M     #套公式
    return answer_datas
    
#区间型指标 -> 极大型指标
def dataDirection_3(datas, x_min, x_max):
    M = max(x_min - np.min(datas), np.max(datas) - x_max)
    answer_list = []
    for i in datas:
        if(i < x_min):
            answer_list.append(1 - (x_min-i) /M)      #套公式
        elif( x_min <= i <= x_max):
            answer_list.append(1)
        else:
            answer_list.append(1 - (i - x_max)/M)
    return np.array(answer_list)

def Standard(datas):
    K = np.power(np.sum(pow(datas,2),axis = 0),0.5)
    for i in range(len(K)):
        datas[: , i] = datas[: , i] / K[i]
    return datas

def Score(sta_data):
    z_max = np.amax(sta_data , axis=0)
    z_min = np.amin(sta_data , axis=0)
    # 计算每一个样本点与最大值的距离
    tmpmaxdist = np.power(np.sum(np.power((z_max - sta_data) , 2) , axis = 1) , 0.5)  # 每个样本距离Z+的距离
    tmpmindist = np.power(np.sum(np.power((z_min - sta_data) , 2) , axis = 1) , 0.5)  # 每个样本距离Z+的距离
    score = tmpmindist / (tmpmindist + tmpmaxdist)
    score = score / np.sum(score)   #归一化处理
    return score

def read(file):
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet = wb.sheet_by_index(0)#通过索引获取表格
    rows = sheet.nrows # 获取行数
    all_content = []        #存放读取的数据
    for j in range(0, 5):       #取第1~第4列对的数据
        temp = []
        for i in range(0,rows) :
            cell = sheet.cell_value(i, j)   #获取数据 
            temp.append(cell)           
        all_content.append(temp)    #按列添加到结果集中
        temp = []
    return np.array(all_content)

file = 'D:\日常应用\学习资料（课堂PPT等等）\数学建模\宋DM全生命周期的能耗与排放.xlsx'
answer1 = read(file)        #读取文件
answer1=np.transpose(answer1)
answer2 = []
for i in range(0, 5):       #按照不同的列，根据不同的指标转换为极大型指标，因为只有四列
        answer = None
        answer = dataDirection_1(answer1[i])
        answer2.append(answer)
answer2 = np.array(answer2)         #将list转换为numpy数组
answer3 = Standard(answer2)            #数组正向化
data1 = Score(answer3)            
data = pd.DataFrame(data1)        #计算得分
print(data)