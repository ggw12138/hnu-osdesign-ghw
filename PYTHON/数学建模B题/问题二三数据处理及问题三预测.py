import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

data1 = pd.read_csv('D:\VSCode\code\PYTHON\数学建模B题\附件1：sale_info.csv')
data2 = pd.read_csv('D:\VSCode\code\PYTHON\数学建模B题\附件2：prod_info.csv')
data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data1['date_rcd'] = pd.to_datetime(data1['date_rcd'])  # 日期格式化
order_data = data1.sort_values(by=['date_rcd'])    # 按日期排序
order_data = order_data.set_index('date_rcd')     # 以日期为下标
data1_values = order_data['2019-06-01':'2019-09-30']  # 截取六月到十月的数据

june = order_data['2019-06-01':'2019-06-30']  # 截取六月数据
june = np.array(june.values)
july = order_data['2019-07-01':'2019-07-31']  # 截取七月数据
july = np.array(july.values)
august = order_data['2019-08-01':'2019-08-31']  # 截取八月数据
august = np.array(august.values)
september = order_data['2019-09-01':'2019-09-30']  # 截取九月数据
september = np.array(september.values)
october = order_data['2019-10-01':'2019-10-31']  # 截取十月数据
october = np.array(october.values)
november = order_data['2019-11-01':'2019-11-30']  # 截取十一月数据
november = np.array(november)
december = order_data['2019-12-01':'2019-12-31']  # 截取十二月数据
december = np.array(december)

newweek = []
oldweek = []
a = '2019-10-01'
a = pd.to_datetime(a)
c = pd.to_datetime('2019-07-09')

for i in range(12):
    b = a + datetime.timedelta(days=6)
    newweek.append(np.array(order_data[a:b]))
    a = b + datetime.timedelta(days=1)
    d = c + datetime.timedelta(days=6)
    oldweek.append(np.array(order_data[c:d]))
    c = d + datetime.timedelta(days=1)

lit = [june, july, august, september, october, november, december]

data1_values = np.array(data1_values.values)
data2_values = np.array(data2.values)
smean = data2_values[:, 3]
smean = set(list(smean))

smean_family = {}  # 小类的所有成员
smean_sales = {}  # 小类对应的总销售额
skc_smean = {}  # 每个商品对应的小类标签
for i in smean:
    smean_family[i] = []
    smean_sales[i] = 0

for i in range(data2_values.shape[0]):
    smean_family[data2_values[i, 3]].append(data2_values[i, 0])

for key, values in smean_family.items():
    for i in range(len(values)):
        skc_smean[smean_family[key][i]] = key

for i in range(data1_values.shape[0]):
    if skc_smean.get(data1_values[i, 0]) == None:
        continue
    else:
        smean_sales[skc_smean[data1_values[i, 0]]] += data1_values[i, 2]

final_smean = sorted(smean_sales.items(),
                     key=lambda item: item[1], reverse=True)

final_smean = final_smean[0:10]
datat = pd.read_excel(r'D:\VSCode\code\PYTHON\前十小类及总销售额.xlsx')
datat = pd.DataFrame(datat)
datat = datat.values
toptensmean = datat[:, 0]

topten = {}
ftopten = {}
for i in range(len(toptensmean)):
    topten[toptensmean[i]] = 0
    ftopten[toptensmean[i]] = []

for i in range(len(lit)):
    for k in range(len(toptensmean)):
        topten[toptensmean[k]] = 0
    for j in range(lit[i].shape[0]):
        if skc_smean.get(lit[i][j][0]) == None:
            continue
        else:
            if topten.get(skc_smean.get(lit[i][j][0])) == None:
                continue
            else:
                topten[skc_smean.get(lit[i][j][0])] += lit[i][j][2]
    for key, values in topten.items():
        ftopten[key].append(values)

newweektop1 = []
oldweektop1 = []
for i in range(12):
    a = 0
    b = 0
    for j in range(newweek[i].shape[0]):
        if skc_smean.get(newweek[i][j][0]) == 27050401:
            a += newweek[i][j][1]
        else:
            continue
    for j in range(oldweek[i].shape[0]):
        if skc_smean.get(oldweek[i][j][0]) == 27050401:
            b += oldweek[i][j][1]
        else:
            continue
    newweektop1.append(a)
    oldweektop1.append(b)
of = []
for i in range(12):
    a = 0
    for j in range(oldweek[i].shape[0]):
        if oldweek[i][j][0] == 596572118723:
            a += oldweek[i][j][1]
        else:
            continue
    of.append(a)

for i in range(12):
    a = 0
    for j in range(newweek[i].shape[0]):
        if newweek[i][j][0] == 596572118723:
            a += newweek[i][j][1]
        else:
            continue
    of.append(a)
print(of)
oldweektop1[12:12] = newweektop1


def ExpMove(y, a):
    n = len(y)
    M = np.zeros(n)
    M[0] = (y[0]+y[1])/2
    for i in range(1, len(y)):
        M[i] = a*y[i-1]+(1-a)*M[i-1]
    return M


pre = []
l = [0.2, 0.5, 0.8]
for i in range(12):
    y = oldweektop1[0:(12+i)]
    yt1 = ExpMove(y, 0.2)
    yt2 = ExpMove(y, 0.5)
    yt3 = ExpMove(y, 0.8)
    yl = []
    yl.append(yt1)
    yl.append(yt2)
    yl.append(yt3)
    lis = []
    lis.append(np.sqrt(((y-yt1)**2).mean()))
    lis.append(np.sqrt(((y-yt2)**2).mean()))
    lis.append(np.sqrt(((y-yt3)**2).mean()))
    a = np.argmin(lis, axis=0)
    pre.append(l[a]*y[-1] +
               (1-l[a])*yl[a][-1])


x = list(range(1, 25))
skc = [24.0, 39.0, 22.0, 35.0, 34.0, 11.0, 17.0, 23.0, 11.0, 10.0, 9.0,
       9.0, 7.0, 9.0, 15.0, 14.0, 13.0, 22.0, 7.0, 10.0, 8.0, 7.0, 6.0, 3.0]
y = [6894, 3296, 4048, 3897, 3549, 4780, 3804, 3293, 3257, 3409, 3737, 3519,
     5570, 4560, 3882, 3056, 3623, 4041, 3368, 3963, 3619, 3393, 3339, 3660]
plt.plot(x, y, color='k')
plt.show()
plt.plot(x, skc, color='g')
plt.show()
