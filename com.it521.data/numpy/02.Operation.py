# ndarray的运算
import numpy as np
import matplotlib.pyplot as plt

#
#  逻辑运算
#
# 随机生成一个8行5列的数组 的二维数组
stock_change = np.random.standard_normal((8, 5))

print(stock_change)

# 数组中每个元素只要大于0.5既为true反之为false
# 对每个元素做相应的逻辑判断
# bool索引
bo = stock_change > 0.5
print(bo)

# 取出bo为true的元素的值
# 返回的是一个一维数组
bo_1 = stock_change[bo]
print(bo_1)

# 通用判断
# 判断 stock_change [0:2,0:5]
bo_2 = stock_change[0:2, 0:5] > 0
print(bo_2)
# np.all 判断一个数组内元素是否都是true
bo_3 = np.all(stock_change[0:2, 0:5] > 0)
print(bo_3)
print("bo_3:", bo_3)
# 判断一个数组内的元素是否有true
bo_4 = np.any(stock_change[:5, :] > 0)
print("bo_4:", bo_4)

# 判断前四天股票四天的涨跌幅 大于0置为1 否则为0
# 大于0置为1 否则为0
temp = stock_change[:4, :4] > 0
temp_1 = np.where(temp, 1, 0)
print("temp_1", temp_1)
# 判断前四个股票前四天的涨幅 大于0.5或者小于-0.5的换为1 否则为0

#
# 统计指标
#
stock_change = np.random.standard_normal((8, 5))
# 前四只股票前四天的最大涨幅

temp = stock_change[:4, :4]
print(temp)
# 求每一行的最大值
# axis = 0 按照列进行计算
# axis = 1 按照行进行计算
temp_x = np.max(temp, axis=1)
print(temp_x)

# 求一行的中位数 ()
temp_x = np.median(temp, axis=1)

# 求最大位置值所在的下标
temp_y = np.argmax(temp, axis=1)
print(temp_y)

#
# 矩阵
#

# 什么是矩阵?
# 矩阵,英文matrix 和array的区别矩阵必须是二维的,但是array可以是多维的
# Aij 指第i行,第j列的元素
# 向量 是一种特殊的矩阵

# 矩阵乘法
# 两个矩阵进行运算的方法
# 进行矩阵乘法运算的两个矩阵必须满足:左矩阵的列数要等于右矩阵的行数

# 矩阵乘法的运算规则
# 拿左矩阵的所有行 跟右矩阵的所有列进行运算
# 行和列进行运算的规则是: 拿行和列对应位置的元素相乘 然后再把所有的乘积加起来
# (m行,n列) × (n行,l列) = (m行,l列)

# 矩阵乘法的性质
# 矩阵的乘法不满足交换律  A×B ≠ B×A
# 矩阵的乘法满足结合律: 即 A×(B×C) = (A×B)×C

# 单位矩阵:
# 方阵:一个特殊的矩阵 行数 = 列数
# 单位矩阵就是一个特殊的方阵 从左上角到右下角的对角线(称为主对角线) 上的元素为1 其余元素都为0
# 一般用L或者E标识
# A × l = l × A = A

# 矩阵转置
# 行列互换

# 矩阵逆
# 如矩阵A是一个m × m 矩阵(方阵)
#