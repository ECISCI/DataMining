# Str方法的使用
class Dog:

    def __init__(self):
        self.type = "波斯狗"
        self.age = 2
        self.name = None

    # 魔术方法
    # 当我们打印对象的时候会调用此方法
    def __str__(self):
        return "卧槽"


# <__main__.Dog oop at 0x000001CD5AEB7448>
# 打印对象的内存地址
dog = Dog()
print(dog)
