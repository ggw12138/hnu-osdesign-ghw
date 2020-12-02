import scipy.integrate as spi
import numpy as np
import pylab as pl
# 总共可被感染人口
N1 = 1400050000  # China
# 观察时间
TS = 1.0
# 观察结束时间
ND = 200.0
# 初始易感人数
S0 = N - 1
S1 = N1 - 1
S2 = N2 - 1
S3 = N3 - 1
# 初始感染人数
I0 = 1
INPUT1 = (S1, I0, 0.0)
gamma = 1/14
beta = 1

def diff_eqs(INP, t):
    Y = np.zeros((3))
    V = INP
    Y[0] = - beta * V[0] * V[1]/N2
    Y[1] = beta * V[0] * V[1]/N2 - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y

def SARS()

t = np.arange(0.0, ND+TS, TS)
# odeint 数值求解微分方程
RES = spi.odeint(diff_eqs, INPUT1, t)
x = RES[:, 1]
x = np.array(x)
x = x.reshape(-1, 1)
x = x[10:25]
pl.subplot(111)
pl.plot(RES[:, 0], '-og', label='Susceptible')
pl.plot(RES[:, 1], '-r', label='Infective')
pl.plot(RES[:, 2], '-k', label='Removal')
pl.legend(loc=0)
pl.title('SIR')
pl.xlabel('Time')
pl.ylabel('Numbers')
pl.xlabel('Time')
pl.show()