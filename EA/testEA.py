#-*-coding:utf-8-*-


import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 获取经过mt4处理的数据集
#data = pd.read_csv('XAUUSDtick.csv')
data = pd.read_csv('eu_ExecData.csv')

# 数据x,y分类
X = data.iloc[:, [0, 1]].values
y = data.iloc[:, [2]].values
y = y.ravel()


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.35, random_state=0)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)



# #3. 用sklearn的感知机模型训练数据
# from sklearn.linear_model import Perceptron

# #迭代次数1000次，学习率0.3
# ppn = Perceptron(n_iter = 1000, eta0 = 0.3, random_state = 0)
# ppn.fit(X_train_std,y_train)
# y_pred = ppn.predict(X_test_std)
# print 'Misclassified samples:%d' % (y_test != y_pred).sum()
# print 'Accuracy:%.2f'% accuracy_score(y_test,y_pred)

# print X_test,y_pred

#1. 用逻辑回归模型预测涨跌
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(X_train_std, y_train)
y_pred = lr.predict(X_test_std)
print 'Misclassified samples:%d' % (y_test != y_pred).sum()
print 'Accuracy:%.2f' % accuracy_score(y_test, y_pred)
