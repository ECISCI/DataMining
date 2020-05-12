# 类的定义
class Cat:
    name = "zhangsan"
    age = 1
    pass


# new对象
cat = Cat()
# 拿到对象的属性
catName = cat.name
# 打印
print(catName)


# 类的成员变量定义格式 一
class Dog:

    def __init__(self):
        self.type = "波斯狗"
        self.age = 2
        self.name = None


# new一个Dog对象
dog = Dog()
# 取出成员变量age的值
age = dog.age
# 给狗名字赋值
dog.name = "尼玛"
# 打印名字
print(dog.name)
# 打印年龄
print(age)

# 添加成员变量没有的属性
dog.color = "red"
print(dog.color)
