#-*- encoding:UTF-8 -*-
#誉天暑期训练营
"""是高性能科学计算和数据分析的基础包,包含大量的工具，数组对象(用来表示向量、矩阵、图像等)以及现行代数"""
import numpy as np
arr1=np.array((1,2,3))
# print(arr1)
lst=[100,200,300,400]
arr2=np.array(lst)
# print(arr2)
"""使用array()创建数组时，参数必须是列表或者元组，且不能使用多个数值
arange():如果arange()函数仅用一个参数，代表的是终值，开始值为0;如果仅使用两个参数，步长默认为1

"""
# lst2=[[1,2,3],[4,5,6]]
# arr3=np.array(lst2)
# # print(arr3)
# arr4=np.zeros((3,4))
# # print(arr4)
# arr5=np.empty((3,4))
# # print(arr5)
# arr6=np.arange(0.2,2,0.3)
# # print(arr6)
# arr7=np.linspace(1,6,5)
# # print(arr7)
# arr8=np.random.rand(3,4)
# # print(arr8)
arr0=np.random.rand(3,4)
print(arr0)
# e1=arr0[0,2] #获取第一行的第三个元素
# # print(e1)
# e2=arr0[:2]#获取第1行和第2行的元素
# # print(e2)
# e3=arr0[:,1]#获取所有行第2列元素
# # print(e3)
e4=arr0[1,:]#获取第2行所有元素
# # print(e4)
e5=arr0[:,1:3]
print(e5)
# e6=arr0[:,2]
# print(e6)
'''brr=np.random.rand(2,3)
print(brr)
print(brr.max())
print(brr.min())'''