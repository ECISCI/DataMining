# 导入工具
import numpy as np
import matplotlib.pyplot as plt

#
#  ndarray基本属性
#

# 二维数组
a = np.array([[1, 2, 3], [4, 5, 6]])
# 一维数组 形状表示的表示的元素个数
b = np.array([1, 2, 3, 4])
# 三维数组
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# (2, 3) 形状表示的事(行 列)
print(a.shape)
# (4,) 形状表示的是元素个数
print(b.shape)
# (2, 2, 3) 形状表示的 (层数,行数,列数)
print(c.shape)

# 数组的维数 2
print(a.ndim)
# 数组的维数 1
print(b.ndim)
# 数组的维数 3
print(c.ndim)

# 数组中元素的个数 6
print(a.size)
# 数组中元素的个数 4
print(b.size)
# 数组中元素的个数 12
print(c.size)

# 内存中占用的字节数 4
print(a.itemsize)
# 内存中占用的字节数 4
print(a.itemsize)
# 内存中占用的字节数 4
print(a.itemsize)

# 一个数组元素的长度(字节) int32
print(a.dtype)
# 一个数组元素的长度(字节) int32
print(b.dtype)
# 一个数组元素的长度(字节) int32
print(c.dtype)

#
#  ndarry的基本操作
#

# 生成全0数组
zero = np.zeros([6, 6, 6])
print(zero)


# 生成全1数组
one = np.ones([6, 6, 6])
print(one)

#
#  从现有数组生成
#

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# 生成和a形状一样的全1数组
print(np.ones_like(a))
# 生成和a形状一样的全0数组
print(np.zeros_like(a))

# 复制形式生成新的数组
b = np.array(a)
# 引用的形式生成新的数组
c = np.array(a)
print(b)
print(c)

# 修改a的值
a[0] = 10
print(a)

#
#  生成固定范围的数组
#

# 生成等间隔的序列
# start         序列的起始值
# stop          序列的终止值
# num           要生成的等间隔样例数量，默认为50
# endpoint      序列中是否包含stop值,默认为ture

# 生成等间隔的数组
# 取从指定范围内取指定等间隔取指定数量的元素
a = np.linspace(1, 10, 10)
print(a)

# 从指定范围内从开始值按照指定步长去数一直到结束值为止,不包含结束值
b = np.arange(1, 11, 2)
print(b)

# 生成等比数列 base=2 等比数列的比例
# 等比数列的比例 从底数2的 一次方开始到2十次方
c = np.logspace(1, 10, 10, base=2)
print(c)


#
#  生成随机数组
#

# 在指定范围内随机抽数,抽到这个范围内每个数的概率都是相等的

# 参数为元组 但要把括号去掉
a = np.random.rand(2, 3)
print(a)

b = np.random.uniform(1, 10, (2, 3))
print(b)


#
#  正态分布
#

# 直方图
# 高考一分一档
# 人的寿命

# 在平局分这个位置 人数达到最大值
# 离平均分越远人数就越少
# 人数的分布会关于平均分对称

#   4.2.正态分布的应用
#       生活与生产科学实验中很多堆积变量的概率分布都可以近似地使用正态分布来描述

#   4.3.正态分布的特点
#       平均值和标准差决定的
#
#       4.3.1 方差
#       衡量的事数据偏离平均值的平均程度


# 正态分布抽样生成随机数

# 标准正态分布抽样
# 正态分布随机生成数组
a = np.random.randn(2, 3)
print(a)

# loc 平均值,scale方差
np.random.normal(loc=1, scale=1, size=(2, 3))

# 标准正态分布抽样
np.random.standard_normal((2, 3))

# 绘制均匀分布抽样生成的数据直方图
x = np.random.uniform(-10, 10, 10000000)
# 创建画布
plt.figure(figsize=(20, 8))
# 绘制图像
plt.hist(x, bins=1000)
# 显示图像
plt.show()

# 绘制正态分布抽样生成的数据直方图
x_2 = np.random.standard_normal((10000000,))
# 创建画布
plt.figure(figsize=(20, 8))
# 绘制图像
plt.hist(x_2, bins=1000)
# 显示图像
plt.show()


#
#  ？？？
#

# 随机生成一个8行5列的数组
stock_change = np.random.standard_normal((8, 5))
# print(stock_change)

# # 取第一行数据
# stock_change[0, :]
# # 冒号索引取前面两行数据
# stock_change[:2, :]
# 冒号索引取前面4行中的 第二行和第三行
# 切片的方法,每个维度用冒号索引进行切片,有多少个维度就传多少个冒号索引
# stock_change[:4:2, :]

# 修改第一行 第一列的第一个值
stock_change[0, 0] = 10

# 形状修改
temp = np.linspace(1, 12, 12)
print(temp)
# 生成新的数组返回,不修改原数组
res = temp.reshape((3, 4))
# 修改原数组的形状
temp.resize((3, 4))

# 转置操作
print(res)
print(temp)

# 转置操作 行列互换
print(temp.T)

# 修改元素在内存中的存储类型
# 需要用变量接收一下,然后去打印变量的值和类型
res_3 = temp.astype(np.int64)
print(res_3)
print("res_3:", res_3.dtype)

res_4 = temp.tostring()
print(res_4)

# 还原数据为 数据类型为float64 reshape为3行4列
# 把序列化数据转回ndarray对象
res_5 = np.frombuffer(res_4, dtype=np.float64).reshape((3, 4))
print("res_5:", res_5)

#
#  数组去重
#
temp = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])

print(temp)

# 剔除数组中重复的元素,以一维数组的形式返回
res = np.unique(temp)
# 去重后只能返回一位数组
print(res)
