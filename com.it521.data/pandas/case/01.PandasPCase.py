import pandas as pd
import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt

# pandas 案例

# 读取电影CSV中的数据
data = pd.read_csv('/data/IMDB-Movie-Data.csv');

#
# 我们想知道这些电影数据中评分的平均分 导演的人数等信息 我们应该怎么获取
#

# 求一列的平均分
menan = data['Rating'].mean()
print('$$$$$ 电影平均分 $$$$$')
print(menan)

# 导演人数 去重
unique = np.unique(data['Director'])
print('$$$$$ 去重后的导演表 $$$$$')
print(unique)
# 统计总共有多少个导演
unique_size = unique.size
# shape返回数组的形状 是一个元组 取出第一个元素与 unique.size 得到结果是一致的
# unique.shape[0]
print('$$$$$ 统计有多少个导演 $$$$$')
print(unique_size)

#
# 对于这一组电影数据 如果我们想 rating runtime的分布情况 应该如何呈现数据
#

# 绘制直方图

# 创建画布
plt.figure(figsize=(20, 8))

# 绘制图像
res = plt.hist(data['Rating'], bins=20)

# 设置X轴刻度
plt.xticks(res[1])
print(res)
# 显示图像
# plt.show()

#
# 对于一组电影数据 如果我们希望统计电影分类的情况 应该如何处理数据
#

# 1.拿到所有的电影类型
movie_type = data['Genre']
print('$$$$$ movie_type $$$$$')
print(movie_type)

action_temp = [i.split(',') for i in data['Genre']]
print('$$$$$ action_temp $$$$$')
print(action_temp)

# 对嵌套数据进行双重循环 并通过 np.unique方式把数组中的元素进行去重
action_list = np.unique([i for j in action_temp for i in j]);
print('$$$$$ action_list $$$$$')
print(action_list)

# 构建一个记录电影类型数量的容器 Series
action_s = pd.Series(np.zeros((len(action_list),)), index=action_list)
print('$$$$$ action_s zero  $$$$$')
print(action_s)

# 遍历所有的电影 统计电影类型的数量
for i in action_temp:
    for j in i:
        action_s[j] += 1

print('$$$$$ action_s result $$$$$')
print(action_s)
