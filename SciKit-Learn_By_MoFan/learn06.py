#-*- coding: utf-8 -*-  

#6.sklearn model的属性与功能

from sklearn import datasets
from sklearn.linear_model import LinearRegression 

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target


model = LinearRegression()
model.fit(data_X,data_y)

# print(model.predict(data_X[:4,:]))

#print(model.coef_) #y =0.1x +0.3, 这里的 model.coef_就是对应公式的x
#print(model.intercept_) #y =0.1x +0.3, 这里的 model.intercept_就是对应公式的0.3

##获取model模型参数
#print(model.get_params())

#模型打分，模型使用data_X数据进行预测，然后与data_y进行对比之后打分
print(model.score(data_X,data_y))

