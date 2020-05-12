import numpy as np
import pandas as pd

# DataFrame的常用属性和方法
# 创建一个随机的二维数组
stock_change = np.random.standard_normal((8, 10))

#
# DataFrame的基本操作
#

# 生成股票名字列表
codes = ['股票' + str(i) for i in range(8)]
# 从 20200403 开始 取10天的日期 跳过周末
date = pd.date_range('20200430', periods=10, freq='B')

# 添加行索引 列索引
pd_data = pd.DataFrame(stock_change, index=codes, columns=date);
print("###### pd_data ######")
print(pd_data)

# 获取数据
data_values = pd_data.values
print("###### 数据 ######")
print(data_values)

# 获取行索引
data_index = pd_data.index
print("###### 行索引 ######")
print(data_index)

# 获取列索引
data_columns = pd_data.columns
print("###### 列索引 ######")
print(data_columns)

# 获取二维数组数据形状
data_shape = pd_data.shape
print("###### 矩阵的形状 ######")
print(data_shape)

# 行列互换
data_change = pd_data.T
print("###### 行列互换 ######")
print(data_change)

# 只看前面三行数据  不传整数值 默认看前五行
data_head = pd_data.head(3)
print("###### 只看前面三行数据 ######")
print(data_head)

# 只看后三行数据  不传整数值 默认看前五行
data_tail = pd_data.tail(3)
print("###### 只看末尾三行数据 ######")
print(data_tail)

# 索引设置 生成新的index列表
new_index = ['股票_' + str(i) for i in range(8)]
print("###### new_index ######")
print(new_index)

#
# 重置索引
#

# 重置索引 1 替换旧索引
pd_data.index = new_index
print("###### 带有新的索引的数据 ######")
print(pd_data)

# 重置索引 2 参数 drop=True 如果不添加默认会加入之前索引(不会丢掉之前的索引)
pd_data.reset_index(drop=True)
print("###### 重置索引 ######")
print(pd_data)

# 重置索引 3 把某一列设置为新索引
df = pd.DataFrame({'month': [1, 4, 7, 10], 'year': [2012, 2014, 2013, 2014], 'sale': [55, 21, 22, 31]})
df.set_index('month')
print("###### 把某一列设置为新索引 ######")
print(df)

# 重置索引 4 把某些列设置为新的索引
res = df.set_index(['month', 'year'])
print("###### 把某些列设置为新的索引 ######")
print(res)
print("###### 多层索引 ######")
print(res.index)
