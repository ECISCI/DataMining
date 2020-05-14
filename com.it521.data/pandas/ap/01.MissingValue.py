import pandas as pd
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 缺失值
# 学习目标
# 说明 Pandas     的缺失值类型
# 应用 replace    实现数据的替换
# 应用 dropna     实现缺失值删除
# 应用 fillna     实现缺失值填充
# 应用 isnull     判断是否有缺失数据NaN

# 处理缺失值 删除 填充  IMDB-Movie-Data.csv

# 读取CSV文件
data_movie = pd.read_csv('H://DataMining/data/IMDB-Movie-Data.csv')
print("###### 读取数据 ######")
print(data_movie)

#
# 判断是否有缺失值
#

# 第一种方法 判断是否有缺失值
# 判断每个元素是否是NaN
data_is_null = pd.isnull(data_movie)
# print("###### data_is_null ######")
# print(data_is_null)
# 判断data_is_null 是否有True
# 使用ndarray中的方法判断是否有True
data_np = np.any(data_is_null)
print("###### data_np ######")
print(data_np)

# 第二种方法 判断是否有缺失值
# 判断每个元素是否是NaN
data_is_null_02 = pd.notnull(data_movie)
data_np_02 = np.any(data_is_null_02)
print("###### data_np_02 ######")
print(data_np_02)

#
# 缺失值的处理
#
# 第一种处理方式 删除缺失值
data_movie_new_01 = data_movie.dropna()
print("###### data_movie_new_01 ######")
print(data_movie_new_01)

# 第二种处理方式 替换缺失值 指定中位数
data_movie_new_02 = data_movie.fillna(value=data_movie.median())
print("###### data_movie_new_02 ######")
print(data_movie_new_02)

# 读取网络数据
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
print("###### wis ######")
print(wis)
# 把一些其它值标记的缺失值，替换成np.nan
wis = wis.replace(to_replace='?', value=np.nan)
# 在进行缺失值的处理 删除
wis_new = wis.dropna()

print("###### wis_new ######")
print(wis_new)
