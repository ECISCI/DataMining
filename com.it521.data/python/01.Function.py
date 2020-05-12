# 定义一个函数
def say():
    print("hello")


# 调用函数
say()


# 比较两个数值哪个大
def max(a, b):
    """文档注释"""

    # 函数内调用另一个函数
    say()
    if (a > b):
        return a
    else:
        return b


# 得到函数的返回值
a = max(5, 9)
print(a)
