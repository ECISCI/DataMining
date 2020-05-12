# numpy的使用

# 导入工具包
import numpy as np
import random
import time

# 创建了一个ndarray对象
score = np.array([[80, 89, 86, 67, 79], [78, 97, 89, 67, 81], [90, 94, 78, 67, 74]
                     , [91, 91, 90, 67, 69], [76, 87, 75, 67, 86], [70, 79, 84, 67, 84]
                     , [94, 92, 93, 67, 64], [86, 85, 83, 67, 80]])

print(score)
print(type(score))

# numpy与Python list的效率对比
a = []
for i in range(100000000):
    a.append(random.random())

# 创建ndarray对象
b = np.array(a)
