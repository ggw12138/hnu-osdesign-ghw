#-*- encoding:UTF-8 -*-
#誉天暑期训练营
"""2D绘图库，是一套面对对象的绘图库，因为用它来绘制图表中的每个绘图元素，Line2D,文字Text pyplot"""
import matplotlib.pyplot as plt
import numpy as np
#创建绘图对象
plt.figure(figsize=(6,4))#设定图像的宽度和高度
x=np.arange(0,np.pi*4,0.01)
y=np.cos(x)
plt.plot(x,y,"k-",linewidth=2.0)#x,y分别的意思是设置x,y轴的数据 g- 代表图形的颜色和线形
#设置x轴文字
plt.xlabel("x")
#设置y轴文字
plt.ylabel("cos(x)")
#设定y轴范围
plt.ylim(-1,1)
#设定图标标题
plt.title("y=cos(x)")
plt.grid(True)
plt.show()

