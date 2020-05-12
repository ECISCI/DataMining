import pandas as pd
import matplotlib.pyplot as plt

# DataFrame的逻辑运算

data = pd.read_csv('H://DataMining/data/stock_day.csv')

#
# 算术运算
#

# 切出其中一列 然后列值每个元素值都+10
data_add_01 = data['low'].add(10).head(5)
print("###### data_add_01 ######")
print(data_add_01)

# 切出两列 并把两列的值进行相加
data_add_02 = data['low'].add(data['close']).head(5)
print("###### data_add_02 ######")
print(data_add_02)

#
# 逻辑运算
#
data_logical_operation_01 = data['p_change'].head() > 0
print("###### data_logical_operation_01 ######")

print(data_logical_operation_01)

# 布尔索引 满足 p_change 全部大于0的数据集整合出来
data_logical_operation_02 = data.head()[data_logical_operation_01]
print("###### data_logical_operation_02 ######")
print(data_logical_operation_02)

# query
# query(expr) expr查询字符串
data_query_01 = data.query('p_change > 2 & open > 15').head(5)
print("###### data_query_01 ######")
print(data_query_01)

# isin(values)
# 例如判断 'turnover' 是否为 4.19,2.39

data_is_in = data['turnover'].isin([2.39]).head()
print("###### data_is_in ######")
print(data_is_in)

# 取出 turnover 的值为2.39 或者等于1.53 的样本
data_is_in_02 = data['turnover'].isin([2.39, 1.53])
data_is_in_03 = data[data_is_in_02]
print("###### data_is_in_03 ######")
print(data_is_in_03)

#
# 统计运算
#

# describe() 综合分析:能够直接得出很多统计结果 count mean std min max 等
data_describe_01 = data.describe()
print("###### data_describe_01 ######")
print(data_describe_01)

# 求最大值

# 每一列的最大值
data_max_01 = data.max()

print("###### data_max_01 ######")
print(data_max_01)

# 求open 和 p_change 最大值
data_max_02 = data['open'].max()

print("###### data_max_02 ######")
print(data_max_02)

#
# 累计统计函数
#

# min 统计指标是一列数据得到一个值
# cumsum 一列数据得到新的一列数据

# 按照时间升序进行排序
data_sort = data.sort_index()
print("###### data_sort ######")
print(data_sort)

# 统计数据累计变化值
data_cumsum = data_sort['price_change'].cumsum()
print("###### data_cumsum ######")
print(data_cumsum)

# 绘制折线图
data_cumsum.plot()
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("股票价格变化图")
# plt.show()


#
# 自定义运算
#
# data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)


# 自定义函数
def fun_1(x):
    return x.max() - x.min()


data_open_close = data[['open', 'close']].apply(fun_1, axis=0)
# data_open_close = data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)
print(data_open_close)
