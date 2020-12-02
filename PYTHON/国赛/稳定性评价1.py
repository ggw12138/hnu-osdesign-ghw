import xlwt
import numpy as np
import pandas as pd
import datetime
data = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\附件1：123家有信贷记录企业的相关数据.xlsx', sheet_name='销项发票信息')

data = pd.DataFrame(data)
data = data.set_index('企业代号')
Enteprisecode = data.index  # 企业代号
Enteprisecode = list(set(Enteprisecode))  # 企业代号


springbegin = pd.to_datetime('2017-01-01')
springend = pd.to_datetime('2017-03-31')
summerbegin = pd.to_datetime('2017-04-01')
summerend = pd.to_datetime('2017-06-30')
fallbegin = pd.to_datetime('2017-07-01')
fallend = pd.to_datetime('2017-09-30')
winterbegin = pd.to_datetime('2017-10-01')
winterend = pd.to_datetime('2017-12-31')


dictenterprise = {}
dictbuyer = {}
seasons = np.zeros((3, 16))  # 16个季度，每季度销售金额，交易次数，退货额
for value in Enteprisecode:
    data1 = data[value:value]  # 读取各个企业的销项发票信息
    data1 = np.array(data1)
    buyers = data1[:, 2]
    buyers = list(set(buyers))
    for buyer in buyers:
        for i in range(data1.shape[0]):
            if (data1[i][2] == buyer):
                for j in range(4):
                    if((data1[i][1] >= pd.to_datetime(springbegin+datetime.timedelta(days=365*j))) and (data1[i][1] <= pd.to_datetime(springend+datetime.timedelta(days=365*j)))):
                        seasons[0][j*4] += data1[i][3]
                        seasons[1][j*4] += 1
                        if(data1[i][3] < 0):
                            seasons[2][j*4] += data1[i][3]
                    elif((data1[i][1] >= pd.to_datetime(summerbegin+datetime.timedelta(days=365*j))) and (data1[i][1] <= pd.to_datetime(summerend+datetime.timedelta(days=365*j)))):
                        seasons[0][1+j*4] += data1[i][3]
                        seasons[1][1+j*4] += 1
                        if(data1[i][3] < 0):
                            seasons[2][1+j*4] += data1[i][3]
                    elif((data1[i][1] >= pd.to_datetime(fallbegin+datetime.timedelta(days=365*j))) and (data1[i][1] <= pd.to_datetime(fallend+datetime.timedelta(days=365*j)))):
                        seasons[0][2+j*4] += data1[i][3]
                        seasons[1][2+j*4] += 1
                        if(data1[i][3] < 0):
                            seasons[2][2+j*4] += data1[i][3]
                    elif((data1[i][1] >= pd.to_datetime(winterbegin+datetime.timedelta(days=365*j))) and (data1[i][1] <= pd.to_datetime(winterend+datetime.timedelta(days=365*j)))):
                        seasons[0][3+j*4] += data1[i][3]
                        seasons[1][3+j*4] += 1
                        if(data1[i][3] < 0):
                            seasons[2][3+j*4] += data1[i][3]
                    else:
                        continue
        dictbuyer[buyer] = seasons
        seasons = np.zeros((3, 16))
    dictenterprise[value] = dictbuyer
    dictbuyer = {}

with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\稳定性评价数据.txt', 'w') as f:
    for k1 in dictenterprise:
        f.write(str(k1))
        f.write('\n')
        curr_dict = dictenterprise[k1]
        for k2 in curr_dict:
            f.write(str(k2))
            f.write(",")
            curr_dict1 = curr_dict[k2]
            for i in range(3):
                for j in range(16):
                    f.write(str(curr_dict1[i][j]))
                    f.write(",")
            f.write('\n')
        f.write('\n')

