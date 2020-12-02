import numpy as np
import pandas as pd
import datetime
data1 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\复：302家无信贷记录企业相关数据.xlsx', sheet_name='进项发票信息')
data2 = pd.read_excel(
    'D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\复：302家无信贷记录企业相关数据.xlsx', sheet_name='销项发票信息')
data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data1['开票日期'] = pd.to_datetime(data1['开票日期'])
data2['开票日期'] = pd.to_datetime(data2['开票日期'])
data1 = np.array(data1)
data2 = np.array(data2)

season = np.zeros((4, 4))

springbegin = pd.to_datetime('2017-01-01')
springend = pd.to_datetime('2017-03-31')
summerbegin = pd.to_datetime('2017-04-01')
summerend = pd.to_datetime('2017-06-30')
fallbegin = pd.to_datetime('2017-07-01')
fallend = pd.to_datetime('2017-09-30')
winterbegin = pd.to_datetime('2017-10-01')
winterend = pd.to_datetime('2017-12-31')

dictionary = {}
temp = data1[0][0]
correct = data1[0][-1]

for i in range(data1.shape[0]):
    if(temp != data1[i][0]):
        dictionary[temp] = season
        season = np.zeros((4, 4))
        temp = data1[i][0]
    if (data1[i][-1] == correct):
        for j in range(4):
            if((data1[i][2] >= pd.to_datetime(springbegin+datetime.timedelta(days=365*j))) and (data1[i][2] <= pd.to_datetime(springend+datetime.timedelta(days=365*j)))):
                season[j][0] += data1[i][4]
            elif((data1[i][2] >= pd.to_datetime(summerbegin+datetime.timedelta(days=365*j))) and (data1[i][2] <= pd.to_datetime(summerend+datetime.timedelta(days=365*j)))):
                season[j][1] += data1[i][4]
            elif((data1[i][2] >= pd.to_datetime(fallbegin+datetime.timedelta(days=365*j))) and (data1[i][2] <= pd.to_datetime(fallend+datetime.timedelta(days=365*j)))):
                season[j][2] += data1[i][4]
            elif((data1[i][2] >= pd.to_datetime(winterbegin+datetime.timedelta(days=365*j))) and (data1[i][2] <= pd.to_datetime(winterend+datetime.timedelta(days=365*j)))):
                season[j][3] += data1[i][4]
            else:
                continue
    if(i == data1.shape[0]-1):
        dictionary[data1[i][0]] = season
        season = np.zeros((4, 4))


with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\进项数据.txt', 'w') as f:
    for k1 in dictionary:
        f.write(str(k1))
        curr_dict = dictionary[k1]
        f.write('{')#这样子字典没有自动的大括号要自己加
        for i in range(4):
            for j in range(4):
                f.write(str(curr_dict[i][j]))
                f.write(",")
        f.write('}')
        f.write('\n')

dictionary1 = {}
temp1 = data2[0][0]
for i in range(data2.shape[0]):
    if(temp1 != data2[i][0]):
        dictionary1[temp1] = season
        season = np.zeros((4, 4))
        temp1 = data2[i][0]
    if (data2[i][-1] == correct):
        for j in range(4):
            if((data2[i][2] >= pd.to_datetime(springbegin+datetime.timedelta(days=365*j))) and (data2[i][2] <= pd.to_datetime(springend+datetime.timedelta(days=365*j)))):
                season[j][0] += data2[i][4]
            elif((data2[i][2] >= pd.to_datetime(summerbegin+datetime.timedelta(days=365*j))) and (data2[i][2] <= pd.to_datetime(summerend+datetime.timedelta(days=365*j)))):
                season[j][1] += data2[i][4]
            elif((data2[i][2] >= pd.to_datetime(fallbegin+datetime.timedelta(days=365*j))) and (data2[i][2] <= pd.to_datetime(fallend+datetime.timedelta(days=365*j)))):
                season[j][2] += data2[i][4]
            elif((data2[i][2] >= pd.to_datetime(winterbegin+datetime.timedelta(days=365*j))) and (data2[i][2] <= pd.to_datetime(winterend+datetime.timedelta(days=365*j)))):
                season[j][3] += data2[i][4]
            else:
                continue
    if(i == data2.shape[0]-1):
        dictionary1[data2[i][0]] = season
        season = np.zeros((4, 4))


with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\销项数据.txt', 'w') as f:
    for k1 in dictionary1:
        f.write(str(k1))
        curr_dict = dictionary1[k1]
        f.write('{')#这样子字典没有自动的大括号要自己加
        for i in range(4):
            for j in range(4):
                f.write(str(curr_dict[i][j]))
                f.write(",")
        f.write('}')
        f.write('\n')