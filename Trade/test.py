

import tushare as ts

df = ts.get_realtime_quotes(['002873',  '000728','002040'])#600340

# def computer(x):


# for data in df
# 	print((data['price']-data['open'])/data['open'])


print(df[['price', 'pre_close']])
