# 静态方法

class Dog:

    def __init__(self):
        self.name = "zhangsan"
        self.age = 11

    @staticmethod
    def show():
        print("汪汪叫")


# 对象可以调用
dog = Dog()
dog.show()
# 类名可以调用
Dog.show()
