import numpy as np
x = [[np.arange(10)],[np.arange(10)]]
L1 = [1, 2, 3, 4, 5]
L2 = [20, 30, 40]
L1[5:5] = L2
print(x[1])