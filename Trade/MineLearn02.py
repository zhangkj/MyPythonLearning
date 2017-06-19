#-*-coding:utf-8-*-

import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

# #读取数据，并创建散点图显示kNN算法结果
# datingDataMat,datingLables = kNN.file2matrix('datingTestSet2.txt')

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLables),15.0*array(datingLables))
# plt.show()

# #分类器针对约会测试网站的测试代码
# kNN.datingClassTest()


# #约会网站预测函数
# kNN.classifyPerson()


# 使用K-近邻算法识别手写数字
# kNN.handwritingClassTest()

# KNN_trader
# 前三天change，今天change，明日change

# Getstock data
# import tushare as ts

# df = ts.get_hist_data('000875')
# #直接保存
# df.to_csv('000875.csv',columns=['open','high','low','close'])


def fileCSV2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = zeros((numberOfLines - 5, 2))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    dataIndex = 0
    dataList = []
    for line in fr.readlines():
        line = line.strip()
        # print(line)
        listFromLine = line.split(',')
        close = listFromLine[-1]
        dataList.append(close)

        index += 1

        if(index < 6):
            continue
        #print(numberOfLines,float(close), dataList[-5])
        Nextchange = (float(dataList[-1]) -
                      float(dataList[-2])) / float(dataList[-2])
        Prechange = (float(dataList[-3]) -
                     float(dataList[-5])) / float(dataList[-5])
        CurChange = (float(dataList[-2]) -
                     float(dataList[-3])) / float(dataList[-3])
        NewLine = [Prechange, CurChange]

        returnMat[dataIndex, :] = NewLine[0:2]
        flag = 1 if Nextchange > 0 else (-1 if Nextchange < 0 else 0)
        classLabelVector.append(flag)
        dataIndex += 1
    return returnMat, classLabelVector


def TradingClassTest():
    hoRatio = 0.50  # hold out 10%
    datingDataMat, datingLabels = fileCSV2matrix(
        '000875.csv')  # load data setfrom file
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = kNN.classify0(normMat[i, :], normMat[
            numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))
    print errorCount


TradingClassTest()

# mat, lable = fileCSV2matrix('000875.csv')
# print(mat[:10, :])
