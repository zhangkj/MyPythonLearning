

import tushare as ts

df = ts.get_realtime_quotes(['002774','002352','601766'])

print(df[['price','pre_close']])

