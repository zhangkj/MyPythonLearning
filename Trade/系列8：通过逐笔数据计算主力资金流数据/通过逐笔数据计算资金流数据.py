# -*- coding: utf-8 -*-
"""
作者：邢不行

本系列帖子“量化小讲堂”，通过实际案例教初学者使用python、pandas进行金融数据处理，希望能对大家有帮助。

必读文章《10年400倍策略分享-附视频逐行讲解代码》：http://bbs.pinggu.org/thread-5558776-1-1.html

所有系列文章汇总请见：http://bbs.pinggu.org/thread-3950124-1-1.html

想要快速、系统的学习量化知识，可以参与我与论坛合作开设的《python量化投资入门》视频课程：http://www.peixun.net/view/1028.html，我会亲自授课，随问随答。
参与课程还可以免费加入我的小密圈，我每天会在圈中分享量化的所见所思，圈子介绍：http://t.xiaomiquan.com/BEiqzVB

微信：xbx_laoshi，量化交流Q群(快满)：438143420，有问题欢迎交流。

文中用到的A股数据可在www.yucezhe.com下载，这里可以下载到所有股票、从上市日起的交易数据、财务数据、分钟数据、分笔数据、逐笔数据等。
"""
import os
import pandas as pd

# ========== 遍历数据文件夹中所有股票文件的文件名，得到股票文件名列表file_list
file_list = []
for root, dirs, files in os.walk('zhubi-2015-05-19/data'):  # 注意：这里请填写数据文件在您电脑中的路径
    if files:
        for f in files:
            if '.csv' in f:
                file_list.append(f.split('.csv')[0])


# ========== 根据上一步得到的文件名列表，遍历所有股票，计算每个股票的资金流数据，放入output变量
output = pd.DataFrame()

# ===遍历每个股票
for f in file_list:
    code = f.split()[-1].strip()  # 读取股票代码
    print code

    # 读取数据
    stock_data = pd.read_csv('zhubi-2015-05-19/data/' + f + '.csv',
                             parse_dates=[0])  # 注意：这里请填写数据文件在您电脑中的路径，注意斜杠方向

    stock_data['Money'] = stock_data['Volume'] * stock_data['Price']  # 计算每笔交易成交额

    l = len(output)
    output.loc[l, 'code'] = code
    output.loc[l, '平均每笔交易成交量'] = stock_data['Volume'].mean()

    # 计算资金流入流出
    data = stock_data.groupby('BuySell')['Money'].sum()
    if 'B' in data.index:
        output.loc[l, '资金流入'] = data['B']
    if 'S' in data.index:
        output.loc[l, '资金流出'] = data['S']

    # 计算主力资金流入流出
    data = stock_data[stock_data['Volume'] > 50000].groupby('BuySell')['Money'].sum()
    if 'B' in data.index:
        output.loc[l, '主力资金流入'] = data['B']
    if 'S' in data.index:
        output.loc[l, '主力资金流出'] = data['S']

# ========== 输出每个股票的资金流数据到csv文件，用中文excel或者wps打开查看
output.to_csv('zijinliushuju.csv', index=False, encoding='gbk')#资金流数据

