#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import numpy as np
myarr1=np.arange(12).reshape(3,4)
print(myarr1)
#计算每列的和
print(myarr1.sum(axis=0))
#计算每行和
print(myarr1.sum(axis=1))
#找出列最大值
print(myarr1.max(axis=0))
#找出行的最大值
print(myarr1.max(axis=1))
#计算每行的累计和
print(myarr1.cumsum(axis=1))