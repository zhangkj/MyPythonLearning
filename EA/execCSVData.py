#-*-coding:utf-8-*-

import pandas as pd
import numpy as np

cols = ['date', 'time', 'open', 'high', 'low', 'close', 'volumn']  # 共7列
df = pd.read_csv('ForexData/eu.csv', header=None, names=cols,
                 dtype={cols[2]: float, cols[3]: float, cols[4]: float, cols[5]: float, })
# print(df.head())
# print(df.describe())

# # 通过标签来在多个轴上进行选择
# print(df.loc[0:5, cols[:2]])
# # 获取一个标量
# print(df.loc[0, cols[0]])
# # 快速访问一个标量（与上一个方法等价）
# print(type(df.at[0, cols[3]]))

cols2 = ['pre3change', 'curChange', 'nextChange']
dfResult = pd.DataFrame(columns=cols2)

j=0
for i in df.index:
    #print(df.at[i, cols[5]])
    if(i<3):
    	continue
    #print(i)
    dfResult.at[j, cols2[0]] = df.at[i-1,cols[5]] - df.at[i-3,cols[5]]
    dfResult.at[j, cols2[1]] = df.at[i,cols[5]] - df.at[i-1,cols[5]]
    dfResult.at[j, cols2[2]] = df.at[i+1,cols[5]] - df.at[i,cols[5]]
    j+=1
    if(i >= len(df.index)-2):
        print(dfResult.head())
        break

dfResult[cols2[2]] = np.where(dfResult[cols2[2]]>0,1,-1)
dfResult.to_csv('eu_ExecData.csv',index=False)