from matplotlib import pyplot as plt
import numpy as np
a = 1
t = np.linspace(0 , 2 * np.pi, 1024)
X = 16*pow(np.sin(t),3)
Y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
#plt.plot(Y, X,color='white')
plt.title('heart')
plt.fill_between(X,Y,facecolor='pink')
plt.show()