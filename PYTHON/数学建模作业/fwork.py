'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_excel('D:\VSCode\code\PYTHON\数学建模作业\区域高程数据.xlsx')
a=np.array(data)
row=a.shape[0]
col=a.shape[1]
fig=plt.figure()
new_array = np.zeros((col-row,col))
b=np.vstack((a,new_array))
x=[]
y=[]
z=[]
xx=[]
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        x.append(i)
        y.append(j)
        z.append(a[i,j])
for i in range(a.shape[1]):
    xx.append(i)

ax1=plt.axes(projection='3d') #3d显示
ax1.plot3D(x,y,z,'pink')
plt.show()                    #注释该句可以获得等高线和3d图的合并
plt.contour(xx,xx,b)          #2d显示
plt.scatter(30,0,c='red')
plt.scatter(43,30,c='red')
plt.show()
'''

#2.6
#读文件
import pandas as pd
import xlrd
h=pd.read_excel('D:\VSCode\code\PYTHON\数学建模作业\区域高程数据.xlsx',userows=list(range(0,875)),usecols=list(range(0,1166)),header=None)
#画三维图
import pylab as plt
import numpy as np
fig=plt.figure()
ax=fig.gca(projection='3d')
x=np.arange(0,58250,50)
y=np.arange(0,43700,50)
x,y= np.meshgrid(x, y)
surf=ax.plot_surface(x, y, h,cmap='coolwarm')
fig.colorbar(surf)
plt.show()
#画等高线图
plt.contour(x,y,h)
plt.scatter(x[0,0],y[30,30],color='r',marker='.',edgecolors='g',s=200)
plt.scatter(x[30,30],y[43,43],color='r',marker='.',edgecolors='g',s=200)
plt.show()
#求该区域地表面积近似值
t=0
x=np.arange(0,58250,50)
y=np.arange(0,43700,50)
for i in np.arange(0,1164):
   for j in np.arange(0,873):
      L1=((x[i]-x[i+1])**2+(h[i][j]-h[i+1][j])**2)**0.5
      L2=((y[j]-y[j+1])**2+(h[i][j]-h[i][j+1])**2)**0.5
      L3=((x[i]-x[i+1])**2+(y[j]-y[j+1])**2+(h[i+1][j]-h[i][j+1])**2)**0.5
      p1=(L1+L2+L3)/2
      L4=((x[i+1]-x[i])**2+(h[i+1][j+1]-h[i][j+1])**2)**0.5
      L5=((y[j+1]-y[j])**2+(h[i+1][j+1]-h[i+1][j])**2)**0.5
      L6=L3
      p2=(L4+L5+L6)/2
      S1=(p1*(p1-L1)*(p1-L2)*(p1-L3))**0.5
      S2=(p2*(p2-L4)*(p2-L5)*(p2-L6))**0.5
      S=S1+S2
      t=t+S
print(t)


        


