import pandas as pd
import numpy as np

data = pd.read_csv("D:\VSCode\code\PYTHON\数学建模B题\附件1：sale_info.csv")
dataie = pd.read_csv("D:\VSCode\code\PYTHON\数学建模B题\附件3：inv_info.csv")
data = pd.DataFrame(data)
dataie = pd.DataFrame(dataie)
data['date_rcd'] = pd.to_datetime(data['date_rcd'])  # 日期格式化
data['skc'] = pd.to_numeric(data['skc'])
order_data = data.sort_values(by=['date_rcd'])    # 按日期排序
order_data = order_data.set_index('date_rcd')     # 以日期为下标

q = order_data['2018-07-01':'2018-10-01']     # 截取7.1到10.1的数据
builtcountrydata = order_data['2018-10-01':'2018-10-07']  # 截取国庆节期间的数据
doubleeledata = order_data['2018-11-11':'2018-11-11']  # 截取双11的数据
doubletwldata = order_data['2018-12-12':'2018-12-12']  # 截取双12的数据
newyeardata = order_data['2018-12-31':'2019-01-01']  # 截取元旦数据

dataie['date_rcd'] = pd.to_datetime(dataie['date_rcd'])  # 日期格式化
dataie['skc'] = pd.to_numeric(dataie['skc'])
order_dataie = dataie.sort_values(by=['date_rcd'])    # 按日期排序
order_dataie = order_dataie.set_index('date_rcd')     # 以日期为下标

bc_ie = order_dataie['2018-10-01':'2018-10-07'] #截取国庆节期间的库存数据
bc_ie=np.array(bc_ie)
ele_ie = order_dataie['2018-11-11':'2018-11-11'] #截取双11的库存数据
ele_ie=np.array(ele_ie)
twl_ie = order_dataie['2018-12-12':'2018-12-12']  # 截取双12的库存数据
twl_ie = np.array(twl_ie)
ny_ie =order_dataie['2018-12-31':'2019-01-01'] #截取元旦的库存数据
ny_ie = np.array(ny_ie)

q1 = q.values[:, 0]
q1 = list(set(list(q1)))           # 商品种类及编号

q = np.array(q)
builtcountrydata = np.array(builtcountrydata)
builtcountry_sales = {}  # 国庆总销售额
builtcountry_num = {}  # 国庆总销量
builtcountry_ie = {} #国庆平均库存
doubleeledata = np.array(doubleeledata)
doubleele_sales = {}  # 双11总销售额
doubleele_num = {}  # 双11总销售量
doubleele_ie = {} #双11平均库存量
doubletwldata = np.array(doubletwldata)
doubletwl_sales = {}  # 双12总销售额
doubletwl_num = {}  # 双12总销售量
doubletwl_ie = {} #双12平均库存量
newyeardata = np.array(newyeardata)
newyear_sales = {}  # 元旦总销售额
newyear_num = {}  # 元旦总销售量
newyear_ie = {} #元旦平均库存量

q1 = q[:, 1]
sumsales = {}  # 7月到10月各种商品对应的总销售额
sumsalesnum = {}  # 7月到10月各种商品对应的总销售量
for i in range(0, q.shape[0]):
    if sumsales.get(q[i, 0]) == None:
        sumsales[q[i, 0]] = q[i, 2]
    else:
        a = sumsales.get(q[i, 0])+q[i, 2]
        sumsales[q[i, 0]] = int(a)

for i in range(0, q1.shape[0]):
    if sumsalesnum.get(q[i, 0]) == None:
        sumsalesnum[q[i, 0]] = q1[i]
    else:
        b = sumsalesnum.get(q[i, 0])+q1[i]
        sumsalesnum[q[i, 0]] = int(b)

final_rank = sorted(
    sumsales.items(), key=lambda item: item[1], reverse=True)  # 从大到小排序总销售额
final_rank = final_rank[0:50]  # 总销售额前50位

salenumtopfifty = {}
for key, value in final_rank:
    salenumtopfifty[key] = sumsalesnum.get(key)  # 前五十位的总销售量
    builtcountry_sales[key] = 0
    builtcountry_num[key] = 0
    doubletwl_sales[key] = 0
    doubletwl_num[key] = 0
    doubleele_sales[key] = 0
    doubleele_num[key] = 0
    newyear_sales[key] = 0
    newyear_num[key] = 0
    builtcountry_ie[key] =0
    doubleele_ie[key] =0
    doubletwl_ie[key]=0
    newyear_ie[key]=0

#以下为四个节日的销量，销售额，库存的计算
for i in range(0, builtcountrydata.shape[0]):
    for key, value in builtcountry_sales.items():
        if builtcountrydata[i, 0] == key:
            a = builtcountry_sales.get(key)+builtcountrydata[i, 2]
            builtcountry_sales[key] = a
            break

for i in range(0, builtcountrydata.shape[0]):
    for key, value in builtcountry_num.items():
        if builtcountrydata[i, 0] == key:
            a = builtcountry_num.get(key)+builtcountrydata[i, 1]
            builtcountry_num[key] = int(a)
            break

for i in range(0, doubleeledata.shape[0]):
    for key, value in doubleele_sales.items():
        if doubleeledata[i, 0] == key:
            a = doubleele_sales.get(key)+doubleeledata[i, 2]
            doubleele_sales[key] = a
            break

for i in range(0, doubleeledata.shape[0]):
    for key, value in doubleele_num.items():
        if doubleeledata[i, 0] == key:
            a = doubleele_num.get(key)+doubleeledata[i, 1]
            doubleele_num[key] = int(a)
            break

for i in range(0, newyeardata.shape[0]):
    for key, value in newyear_sales.items():
        if newyeardata[i, 0] == key:
            a = newyear_sales.get(key)+newyeardata[i, 2]
            newyear_sales[key] = a
            break

for i in range(0, newyeardata.shape[0]):
    for key, value in newyear_num.items():
        if newyeardata[i, 0] == key:
            a = newyear_num.get(key)+newyeardata[i, 1]
            newyear_num[key] = int(a)
            break

for i in range(0, doubletwldata.shape[0]):
    for key, value in doubletwl_sales.items():
        if doubletwldata[i, 0] == key:
            a = doubletwl_sales.get(key)+doubletwldata[i, 2]
            doubletwl_sales[key] = a
            break

for i in range(0, doubletwldata.shape[0]):
    for key, value in doubletwl_num.items():
        if doubletwldata[i, 0] == key:
            a = doubletwl_num.get(key)+doubletwldata[i, 1]
            doubletwl_num[key] = int(a)
            break

for i in range(0, ele_ie.shape[0]):
    for key, value in doubleele_ie.items():
        if ele_ie[i, 0] == key:
            a = doubleele_ie.get(key)+ele_ie[i, 1]
            doubleele_ie[key] = int(a)
            break

for i in range(0, twl_ie.shape[0]):
    for key, value in doubletwl_ie.items():
        if twl_ie[i, 0] == key:
            a = doubletwl_ie.get(key)+twl_ie[i, 1]
            doubletwl_ie[key] = int(a)
            break

for i in range(0, ny_ie.shape[0]):
    for key, value in newyear_ie.items():
        if ny_ie[i, 0] == key:
            a = newyear_ie.get(key)+(ny_ie[i, 1]/2)
            newyear_ie[key] = int(a)
            break

for i in range(0, bc_ie.shape[0]):
    for key, value in builtcountry_ie.items():
        if bc_ie[i, 0] == key:
            a = builtcountry_ie.get(key)+(bc_ie[i, 1]/7)
            builtcountry_ie[key] = int(a)
            break

'''#输出文件
pf = pd.DataFrame(list(builtcountry_ie.items()))
# 指定生成的Excel表格名称
file_path = pd.ExcelWriter('D:\VSCode\code\PYTHON\国庆库存.xlsx')
# 替换空单元格
pf.fillna(' ', inplace=True)
# 输出
pf.to_excel(file_path, encoding='utf-8', index=False)
# 保存表格
file_path.save()'''

'''pf = pd.DataFrame(final_rank)
#指定生成的Excel表格名称
file_path = pd.ExcelWriter('D:\VSCode\code\PYTHON\销售量前50名单.xlsx')
#替换空单元格
pf.fillna(' ',inplace = True)
#输出
pf.to_excel(file_path,encoding = 'utf-8',index = False)
#保存表格
file_path.save()'''

# 折扣处理
data2 = pd.read_csv("D:\VSCode\code\PYTHON\数学建模B题\附件2：prod_info.csv")
data2 = pd.DataFrame(data2)
data2 = np.array(data2)
datay = {}
for i in range(1, data2.shape[0]):
    if data2[i, 1] == 2018:
        datay[data2[i, 0]] = data2[i, 4]
    else:
        continue

tagsales = {}
for key, value in final_rank:
    salenum = salenumtopfifty.get(key)
    if datay.get(key) == None:
        tagsales[key] = sumsales.get(key)/sumsalesnum.get(key)
    else:
        tagsales[key] =datay.get(key)

pf = pd.DataFrame(list(tagsales.items()))
# 指定生成的Excel表格名称
file_path = pd.ExcelWriter('D:\VSCode\code\PYTHON\标签价.xlsx')
# 替换空单元格
pf.fillna(' ', inplace=True)
# 输出
pf.to_excel(file_path, encoding='utf-8', index=False)
# 保存表格
file_path.save()

