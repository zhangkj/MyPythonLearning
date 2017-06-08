#-*- coding: utf-8 -*-  


#8.交叉验证 Cross-validation


import numpy as np 
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target



# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)

# knn = KNeighborsClassifier(n_neighbors=5)
# #训练数据
# knn.fit(X_train,y_train)  
# #预测数据
# # y_pred = knn.predict(X_test)
# print(knn.score(X_test,y_test))


from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt 
k_range = range(1,31)
k_scores=[]
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors=k)
	#loss = cross_val_score(knn,X,y,cv=10,scoring='mean_squared_error')#for regression
	scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')#for classification
	k_scores.append(scores.mean())

plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()