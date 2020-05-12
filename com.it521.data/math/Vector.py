import numpy as np

############################## 《加减数乘》

a = np.array([1, -2])
b = np.array([3, 1])
# 加法
x01 = a + b
# print("加法 x01值:", x01)

# 数乘
x02 = a * 2
# print("数乘 x02值:", x02)

x03 = b * (-3)
# print("数乘 x03值:", x02)


############################## 《点积》
a = np.array([-2, 2])
b = np.array([2, 2])

# 计算点积(内积)
ab_1 = np.inner(a, b)

# 根据夹角余弦计算点积
ab_2 = np.linalg.norm(a) * np.linalg.norm(b) * np.cos(np.pi / 2)

print("计算点积 :", ab_1)
print("根据夹角余弦计算点积 :", ab_2)
