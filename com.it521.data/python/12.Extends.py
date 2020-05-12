# 继承

class Father:
    def __init__(self):
        self.sex = "男"
        self.age = None

    def show(self):
        print("打印")


class XioGang(Father):
    pass


# 直接拿到父类的属性
gang = XioGang()
print(gang.sex)
# 对父类的属性进行赋值
gang.age = 11
print(gang.age)
gang.show()


# 集成的关系图

class Animal:
    pass


class Cat(Animal):
    pass


class HuCat(Cat):
    pass


# 查看类的集成关系图
print(HuCat.__mro__)
