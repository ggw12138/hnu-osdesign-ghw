# 防止不必要的警告
import warnings
warnings.filterwarnings("ignore")
# 引入数据科学基础包
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import seaborn as sns
## 设置属性防止画图中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# 引入机器学习，预处理，模型选择，评估指标
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
#引入本次所使用的波士顿数据集
from sklearn.datasets import load_boston
# 引入算法
from sklearn.linear_model import RidgeCV, LassoCV, LinearRegression, ElasticNet
#对比SVC，是svm的回归形式
from sklearn.svm import SVR
# 集成算法
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
# 载入波士顿房价数据集
boston = load_boston()
# x是特征，y是标签
x=boston.data
y=boston.target
# 查看相关属性
print('特征的列名')
print(boston.feature_names)
print("样本数据量:%d, 特征个数：%d" % x.shape)
print("target样本数据量:%d" % y.shape[0])

# 转化为dataframe形式
x = pd.DataFrame(boston.data, columns=boston.feature_names)
# x.head()
print(x.head())
sns.distplot(tuple(y), kde=False, fit=st.norm)

# 数据分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=28)
# 标准化数据集
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)
print(x_train[0:100])
# 模型的名字
names = ['LinerRegression','Ridge','Lasso','Random Forrest','GBDT','Support Vector Regression','ElasticNet','XgBoost']
# 定义模型
# cv在这里是交叉验证的思想
models = [LinearRegression(),
RidgeCV(alphas=(0.001,0.1,1),cv=3),
LassoCV(alphas=(0.001,0.1,1),cv=5),
RandomForestRegressor(n_estimators=10),
GradientBoostingRegressor(n_estimators=30),
SVR(),
ElasticNet(alpha=0.001,max_iter=10000),
XGBRegressor()]
# 定义R2评分的函数
# def R2(model,x_train, x_test, y_train, y_test):
#     model_fitted = model.fit(x_train,y_train)
#       y_pred = model_fitted.predict(x_test)
#      score = r2_score(y_test, y_pred)
#       return score

def R2(model,x_train,x_test,y_train,y_test):
    model_fitted = model.fit(x_train,y_train)
    y_pred = model_fitted.predict(x_test)
    score = r2_score(y_test, y_pred)
    return score

# 遍历所有模型进行评分
for name,model in zip(names,models):
    score = R2(model,x_train, x_test, y_train, y_test)
    print("{}: {:.6f}, {:.4f}".format(name,score.mean(),score.std()))


# 模型构建
'''
  'kernel': 核函数
  'C': SVR的正则化因子,
  'gamma': 'rbf', 'poly' and 'sigmoid'核函数的系数，影响模型性能
'''
parameters = {'kernel': ['linear', 'rbf'],
              'C': [0.1, 0.5,0.9,1,5],
              'gamma': [0.001,0.01,0.1,1]
}
# 使用网格搜索，以及交叉验证
model = GridSearchCV(SVR(), param_grid=parameters, cv=3)
model.fit(x_train, y_train)
## 获取最优参数
print ("最优参数列表:", model.best_params_)
print ("最优模型:", model.best_estimator_)
print ("最优R2值:", model.best_score_)
## 可视化
ln_x_test = range(len(x_test))
y_predict = model.predict(x_test)
# 设置画布
plt.figure(figsize=(16,8), facecolor='w')
# 用红实线画图
plt.plot(ln_x_test, y_test, 'r-', lw=2, label=u'真实值')
# 用绿实线画图
plt.plot(ln_x_test, y_predict, 'g-', lw = 3, label=u'SVR算法估计值,$R^2$=%.3f' % (model.best_score_))
# 图形显示
plt.legend(loc = 'upper left')
plt.grid(True)
plt.title(u"波士顿房屋价格预测(SVM)")
plt.xlim(0, 101)
plt.show()
