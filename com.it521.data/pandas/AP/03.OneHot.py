import pandas as  pd

# one-hot 编码
# 从数据中学习规律

# 什么是one-hot编码
# 把每个类别生成一个布尔列 这些列中只有一列可以为这个样本取值为1
# 其又被成为热编码

# 为了避免 0,1,2,3 这样的标记给离散数据加上大小关系

# 读取CSV文件中的数据
data = pd.read_csv('H://DataMining/data/stock_day.csv')
# 取出其中的p_change列
data_p_change = data['p_change']
# 对p_change列的数据进行离散化
data_res = pd.cut(data_p_change, 3)
# one-hot编码
one_hot_data = pd.get_dummies(data_res, prefix='abc')
#
print("###### one_hot_data ######")
print(one_hot_data)
