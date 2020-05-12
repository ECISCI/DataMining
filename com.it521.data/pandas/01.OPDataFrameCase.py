import pandas as pd

# DataFrame的基本使用

#
#  读取数据 拿到数据集
#
data = pd.read_csv('H://DataMining/data/stock_day.csv')
# 取出CSV文件中前10行数据 如果不指定head()中的int值则默认取出前五行
data_head = data.head(10)
print("###### data_head ######")
print(data_head)

#
#  通过 中括号索引 [] (取出列名为'close'一列的所有值)
#
data_close = data['close'].head(10)  # Series
print("###### data_close ######")
print(data_close)

#
#  先列后行 (先取出一列值,然后以行值为键取出对应的value)
#
data_close_value = data['close'].head(10)['2018-02-27']
print("###### data_close_value ######")
print(data_close_value)

#
#  通过loc索引  [行,列] 用行列名来索引
#
data_loc = data.loc['2018-02-27', 'close']
data_loc_two = data.loc['2018-02-27', 'close':'low']
print("###### data_loc ######")
print(data_loc)

print("###### data_loc_two ######")
print(data_loc_two)

#
#  通过iloc 通过下标方式索引 用下标来索引(拿出第二行,第二列对应的值)
#
data_iloc = data.iloc[2, 2]
print("###### data_iloc ######")
print(data_iloc)

#
#  通过iloc 通过下标方式索引 用下标来索引(第二列及第二列脚标为2以后的所有数据)
#
data_iloc_x = data.iloc[2, 2:]
print("###### data_iloc_x ######")
print(data_iloc_x)

#
#  使用ix组合索引 (已经废弃) 使用下标 行/列 名进行索引
#

#
#  排序操作
#
data_head_5 = data.head(5)

# 按照p_change从小到达进行排序 (根据 p_change 进行排序)
sort_value_01 = data_head_5.sort_values(by='p_change', ascending=True)
print("sort_value_01", sort_value_01)

# 索引排序 索引降序排序
sort_value_02 = data_head_5.sort_index(ascending=False)
print("sort_value_02", sort_value_02)
