import pandas as pd

# Data consolidation 数据合并
# 目标
# 应用 pd.concat  实现数据合并
# 应用 pd.merge   实现数据合并

# 读取CSV文件中的数据
data = pd.read_csv('H://DataMining/data/stock_day.csv')
# 取出其中的p_change列
data_p_change = data['p_change']
# 对p_change列的数据进行离散化
data_res = pd.cut(data_p_change, 3)
# one-hot编码
one_hot_data = pd.get_dummies(data_res, prefix='abc')
#
# print("###### one_hot_data ######")
# print(one_hot_data)

# 把 one_hot 后的编码后的数据合并到数据集中
data_concat = pd.concat([data, one_hot_data], axis=1)
print("###### data_concat ######")
print(data_concat.head())

# merge 合并
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# inner连接合并数据集 left 左数据集 right 右数据集 on 合并的共有字段 how 合并方式
data_merge = pd.merge(left=left, right=right, on=['key1', 'key2'], how='inner')
print("###### data_merge ######")
print(data_merge)