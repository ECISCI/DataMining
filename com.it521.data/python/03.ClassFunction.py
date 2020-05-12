# 类中的方法
class Dog:

    def __init__(self):
        self.type = "波斯狗"
        self.age = 2
        self.name = None

    def eat(self):
        print("吃骨头")

    def maxAge(self, age):
        print("最大年龄:", age)


dog = Dog()

dog.eat()
dog.maxAge(25)
