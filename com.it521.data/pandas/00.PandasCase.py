import numpy as np
import pandas as pd

# README
stock_change = np.random.standard_normal((8, 10))
print("###### stock_change ######")
print(stock_change)

# 生成股票名字列表
codes = ['股票' + str(i) for i in range(8)]
print("###### codes ######")
print(codes)

# 从 20200403开始 取10天的日期 跳过周末
date = pd.date_range('20200430', periods=10, freq='B')
print("###### date ######")
print(date)
data = pd.DataFrame(stock_change,index= codes,columns=date);
print("###### data ######")
print(data)
