#----------------sklearn的数据库


#-*- coding: utf-8 -*-  

import numpy as np 
from sklearn import datasets
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt


# loaded_data = datasets.load_boston()
# data_X = loaded_data.data
# data_y = loaded_data.target



# #定义model,线性回归
# model = LinearRegression()
# #模型学习
# model.fit(data_X,data_y)

# #print(model.predict(data_X[:4,:]))
# #print(data_y[:4])


#创造一些数据
X,y = datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10)
plt.scatter(X,y)
plt.show()
