#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import numpy as np
# yarr0=np.int32(50*np.random.rand(3,4))
# # print(yarr0)
# yarr1=yarr0.ravel()#用于降低数组的维度
# # print(yarr1)
# yarr0.shape=(6,2)
# print(yarr0)
# yarr2=yarr0.transpose()
# print(yarr2)
# print(id(yarr2))
# print(yarr2.transpose())#专置数组,id值不发生改变
# print(id(yarr2))
yarr0=np.array([[12,31],[32,49],[34,41],[26,34],[43,3],[10,5]])
print(id(yarr0))
yarr0.resize((4,3))
print(yarr0)
print(id(yarr0))