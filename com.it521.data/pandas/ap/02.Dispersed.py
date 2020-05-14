import pandas as pd
import numpy as np

# dispersed 数据离散化


# 1 为什么要离散化
# 连续属性离散化的目的是为了简化数据结构,数据离散化技术可以用来减少给定连续属性值的个数。离散化方法经常作为数据挖掘的工具。

# 2 什么是数据的离散化
# 连续属性的离散化就是在连续属性的值域上,将值域划分为若干个离散的区间,最后用不同的符号或整数 值代表落在每个子区间中的属性值。

data = pd.read_csv('H://DataMining/data/stock_day.csv')
print("###### data ######")
# print(data)

# 取出 p_change 列
data_p_change = data['p_change']

# 进行数据离散化 qcut
# labels 离散化之后每个类别的标记
data_qcut = pd.qcut(data_p_change, 3, labels=['A', 'B', 'C'])
print("###### data_qcut ######")
print(data_qcut)

# 统计各个类别的数量
# data_qcut 把样本平均分到指定数量的类别中
data_qcut_value_counts = data_qcut.value_counts()
print("###### data_qcut_value_counts ######")
print(data_qcut_value_counts)

# cut
# 把区间平均分成指定数量的份数 再对落在每个区间内的样本打上响应区间的标签
data_cut = pd.cut(data_p_change, 3)
data_cut_value_counts = data_cut.value_counts()
print("###### data_cut_value_counts ######")
print(data_cut_value_counts)

# 把区间平均分成指定数量的份数 再落在每个区间内的样本打上相应的标签
data_res = pd.cut(data_p_change, [-100, -7, -5, -3, 0, 3, 5, 7, 100])
print("###### data_res ######")
print(data_res)
# 统计各个类别的数量
data_res_count = data_res.value_counts()
print("###### data_res_count ######")
print(data_res_count)