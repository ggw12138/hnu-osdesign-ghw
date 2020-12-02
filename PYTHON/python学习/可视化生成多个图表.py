#-*- encoding:UTF-8 -*-
#誉天暑期训练营
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# plt.figure(1)#创建图表1
# ax1=plt.subplot(211)#图表1中的子图1
# ax2=plt.subplot(212)#图表1中的子图2
# plt.figure(2)
# x=np.linspace(0,3,50)
# for i in x:
#     plt.figure(2)
#     plt.plot(x,np.exp(i*x/3))
#     plt.sca(ax1)
#     plt.plot(x,np.sin(i*x))
#     plt.sca(ax2)
#     plt.plot(x,np.cos(i*x))
#
# plt.show()
# mu=100
# sigma=20
# x=mu+sigma*np.random.rand(20)
# plt.hist(x,bins=10,color='green',density=True)
# """x：该参数用于指定每个bin(箱子)分布在x轴的位置
#    bins:用于指定bin个数，也就是说是条状图的个数
#    density:值为True时候，本区间的点在所有点中所占的概率
#    color:指定条状图的颜色
# """
# print(x)条状图
# plt.figure(figsize=(6,4))
# y=[10,20,8.45,22,3,2,12]
# x=np.arange(7)
# plt.bar(x,y,color='blue',width=0.5)
# plt.show()
#饼状图
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']='SimHei'
labels=["一季度","二季度","三季度","四季度"]
data=[16,27,25,29]
explodes=[0,0.1,0.1,0]
plt.axes(aspect=1)
plt.pie(x=data,labels=labels,explode=explodes,autopct="%.1f%%",shadow=True)
plt.show()
