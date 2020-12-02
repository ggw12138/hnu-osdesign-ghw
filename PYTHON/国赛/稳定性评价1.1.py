import numpy as np
import pandas as pd

data = pd.read_excel('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\稳定性评价数据.xlsx')
data = pd.DataFrame(data)

data = np.array(data)

codeindex = []

dictionary = {}    # 总交易次数前5
dictionary1 = {}   # 总交易次数前5对应的交易额占比
for i in range(data.shape[0]):
    if(data[i][1] == 1):
        codeindex.append(i)

# 计算前n-1个商家的数据        
for i in range(len(codeindex)-1):
    curr_data = data[np.arange(codeindex[i]+1,codeindex[i+1])]    # 取第[codeindex[i]+1，condeindex[i+1]-1]区间的行数据
    dictbuyers = curr_data[:,0]
    selldata = curr_data[:,1:17]
    totalsell = np.sum(selldata,axis=0)   # 按列求和的到该季度的总交易额
    buyers = {}
    for buyer in dictbuyers:
        buyers[buyer] = 0;    #记录每一个买家对应的排位前5的次数

    seasons = []    # 每季度对应的前5买家
    seasonsale = [] # 每季度对应前五买家的交易额占比
    for k in range(16):
        curr_data1 = sorted(curr_data, key=lambda x:x[k+1],reverse=True)   # 以交易额的列数据为依据进行从大到小排序
        row = len(curr_data1)
        r = 0
        if (row < 5):    # 若买家少于5家的话则全部都取
            r = row
        else:
            r = 5
        for j in range(r):
            if(curr_data1[j][k+1]!=0):
                buyers[curr_data1[j][0]] += 1       # 每进一次前5则加一
        buyer = sorted(buyers.items(), key=lambda item: item[1],reverse=True)   # 对每季度买家排位前5次数进行从大到小排序获得稳定客户ID
        IDbuyer = []
        if(len(buyer) < 5):
            r = len(buyer)
        else:
            r = 5
        for key in range(5):
            if(key<r):
                if(buyer[key][1] != 0 ):        # 如果前5里面有0的买家则不加入前5队列,为Nan
                    IDbuyer.append(buyer[key][0])
                else:
                    IDbuyer.append('Nan')
            else:
                IDbuyer.append('Nan')
        seasons.append(IDbuyer)
        salesaccount = []
        for q in range(5):
            for key in range(row):    
                if(IDbuyer[q]==curr_data1[key][0]):
                    if(totalsell[k]!=0):
                        salesaccount.append(selldata[key][k]/totalsell[k])
                    else:
                        salesaccount.append(0)
                if(IDbuyer[q]=='Nan'):
                    salesaccount.append(0)
                    break
        seasonsale.append(salesaccount)
                    
    dictionary[data[codeindex[i]][0]] = seasons
    dictionary1[data[codeindex[i]][0]] = seasonsale
    
curr_data = data[np.arange(codeindex[-1]+1,data.shape[0])]    # 取最后一个区间区间的行数据
dictbuyers = curr_data[:,0]
selldata = curr_data[:,1:17]
totalsell = np.sum(selldata,axis=0)   # 按列求和的到该季度的总交易额
buyers = {}
for buyer in dictbuyers:
    buyers[buyer] = 0;    #记录每一个买家对应的排位前5的次数

seasons = []    # 每季度对应的前5买家
seasonsale = [] # 每季度对应前五买家的交易额占比
for k in range(16):
    curr_data1 = sorted(curr_data, key=lambda x:x[k+1],reverse=True)   # 以交易金额的列数据为依据进行从大到小排序
    row = len(curr_data1)
    r = 0
    if (row < 5):    # 若买家少于5家的话则全部都取
        r = row
    else:
        r = 5
    for j in range(r):
        if(curr_data1[j][k+1]!=0):
             buyers[curr_data1[j][0]] += 1       # 每进一次前5则加一
    buyer = sorted(buyers.items(), key=lambda item: item[1],reverse=True)   # 对每季度买家排位前5次数进行从大到小排序获得稳定客户ID
    IDbuyer = []
    if(len(buyer) < 5):
        r = len(buyer)
    else:
        r = 5
    for key in range(5):
        if(key<r):
            if(buyer[key][1] != 0 ):        # 如果前5里面有0的买家则不加入前5队列,为Nan
                IDbuyer.append(buyer[key][0])
            else:
                IDbuyer.append('Nan')
        else:
            IDbuyer.append('Nan')
    seasons.append(IDbuyer)
    salesaccount = []
    for q in range(5):
        for key in range(row):    
            if(IDbuyer[q]==curr_data1[key][0]):
                if(totalsell[k]!=0):
                    salesaccount.append(selldata[key][k]/totalsell[k])
                else:
                    salesaccount.append(0)
            if(IDbuyer[q]=='Nan'):
                salesaccount.append(0)
                break
    seasonsale.append(salesaccount)
                    
dictionary[data[codeindex[-1]][0]] = seasons
dictionary1[data[codeindex[-1]][0]] = seasonsale
            
with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\前五ID.txt', 'w') as f:
    for k1 in dictionary:
        f.write(str(k1))
        f.write('\n')
        curr_dict = dictionary[k1]
        for i in range(16):
            for j in range(5):
                f.write(str(curr_dict[i][j]))
                f.write(",")
        f.write('\n')

with open('D:\日常应用\学习资料（课堂PPT等等）\数学建模\国赛题目\CUMCM2020Probelms\C\前五各占比.txt', 'w') as f:
    for k1 in dictionary1:
        f.write(str(k1))
        f.write('\n')
        curr_dict = dictionary1[k1]
        for i in range(16):
            for j in range(5):
                f.write(str(curr_dict[i][j]))
                f.write(",")
        f.write('\n')

    



