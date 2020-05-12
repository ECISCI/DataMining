# matplotlib 折线图

import matplotlib.pyplot as plt
import random

# 入门图
# plt.figure(figsize=(20, 8))
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()

#
#  绘制折线图
#

# 绘制折线图
# 基础绘图 折线图 横坐标,纵坐标
# 展示上海一周的天气
# 实现温度变化的绘制

# 1.先生成fig
# plt.figure(figsize=(10, 10))

# 2.准备数据
# 参数一表示7个点的横坐标 X
# 参数二表示7个点的纵坐标 Y
# XY坐标个数一一对应
# plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])
# 将文件保存到D盘下,并命名为test.png
# plt.savefig("D:\\test.png")

# 3.显示调用
# plt.show()

#
#  温度变化显示
#

# 温度变化显示
# 画出某城市11点到12点1小时内每分钟的温度变化折线图,温度范围在15-18度

# plt.figure(figsize=(20, 8))
#
# # 解决中文乱码问题
# plt.rcParams['font.sans-serif'] = [u'SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 准备数据 上海
# x = range(60)
# x_ch = ["11时{}分".format(i) for i in x]
# y_shanghai = [random.uniform(15, 18) for i in range(60)]
# y_ticks = range(40)
#
# # 准备数据 北京 x轴数据是公用的
# y_beijing = [random.uniform(1, 3) for i in range(60)]
#
# # 添加上海折线图
# plt.plot(x, y_shanghai, color='y', label="上海")
# # 添加北京折线图
# plt.plot(x, y_beijing, color='r', label="北京")
#
# # 添加刻度调解
# # 修改刻度值
#
# # 第一个参数指定显示的X的刻度的列表
# # 第二个参数指定跟第一个餐护士对应的中文
# plt.xticks(x[::5], x_ch[::5])
# plt.yticks(y_ticks[::5])
#
# # 增加标题,坐标描述
# plt.xlabel("时间")
# # 设置Y轴显示文字
# plt.ylabel("温度")
# # 设置标题
# plt.title("沈阳 11点-12点")
#
# # 增加图例的显示
# plt.legend(loc="best")
# plt.show()

#
#  两个城市的温度在多个坐标系中显示
#

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 制造数据
x = range(60)
x_ch = ["11时{}分".format(i) for i in x]
y_shanghai = [random.uniform(15, 18) for i in range(60)]
y_ticks = range(40)
y_beijing = [random.uniform(1, 3) for i in range(60)]

ax[0].plot(x, y_shanghai, label="上海", color='r')
ax[1].plot(x, y_beijing, label="北京", color='b')

# 多个ax里面画图的时候,刻度,标签,必须在相应的坐标系中处理

ax[0].set_xticks(x[::5], x_ch[::5])
ax[0].set_yticks(y_ticks[::5])
ax[1].set_xticks(x[::5], x_ch[::5])
ax[1].set_yticks(y_ticks[::5])

ax[0].set_xlabel("时间")
ax[0].set_ylabel("温度")
ax[0].set_title("上海")
ax[0].set_title("上海市 11点-12点 温度变化图")

ax[1].set_xlabel("时间")
ax[1].set_ylabel("温度")
ax[1].set_title("北京")
ax[1].set_title("北京市 11点-12点 温度变化图")

ax[0].legend(loc="best")
ax[1].legend(loc="best")
plt.show()
