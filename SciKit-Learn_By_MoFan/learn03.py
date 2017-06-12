
import numpy as np 
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target

##print(iris_X[:2,:])
##print(iris_Y)

X_train,X_test,y_train,y_test = train_test_split(iris_X,iris_Y,test_size=0.3)

##print(y_train)

knn = KNeighborsClassifier()
#训练数据
knn.fit(X_train,y_train)  
#预测数据
print(knn.predict(X_test))
#实际真实结果
print(y_test)


#----------------sklearn的数据库