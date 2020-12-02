import numpy as np
import pandas as pd

data = pd.read_excel(r'D:\VSCode\code\PYTHON\前十小类各月总销售额.xlsx')
data = pd.DataFrame(data)
data = data.values

y = data[:, 1:7]
yt = {}
s = {}
yt[0.2] = []
yt[0.5] = []
yt[0.8] = []
s[0.2] = []
s[0.5] = []
s[0.8] = []


def ExpMove(y, a):
    n = len(y)
    M = np.zeros(n)
    M[0] = (y[0]+y[1])/2
    for i in range(1, len(y)):
        M[i] = a*y[i-1]+(1-a)*M[i-1]
    return M


dat1 = []
for i in range(y.shape[0]):
    dat1.append(y[i, :])
    dat = y[i, :]
    yt[0.2].append(ExpMove(dat, 0.2))
    s[0.2].append(np.sqrt(((y-yt[0.2][i])**2).mean()))
    yt[0.5].append(ExpMove(dat, 0.5))
    s[0.5].append(np.sqrt(((y-yt[0.5][i])**2).mean()))
    yt[0.8].append(ExpMove(dat, 0.8))
    s[0.8].append(np.sqrt(((y-yt[0.8][i])**2).mean()))
selection = [0.2, 0.5, 0.8]
yh = []
for i in range(y.shape[0]):
    lis = []
    lis.append(s[0.2][i])
    lis.append(s[0.5][i])
    lis.append(s[0.8][i])
    a = np.argmin(lis, axis=0)
    yh.append(selection[a]*dat1[i][-1] +
              (1-selection[a])*yt[selection[a]][i][-1])

print(yh)
'''pf = pd.DataFrame(yh)
# 指定生成的Excel表格名称
file_path = pd.ExcelWriter('D:\VSCode\code\PYTHON\预测.xlsx')
# 替换空单元格
pf.fillna(' ', inplace=True)
# 输出
pf.to_excel(file_path, encoding='utf-8', index=False)
# 保存表格
file_path.save()
'''