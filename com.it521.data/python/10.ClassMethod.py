# 类方法

class Cat:

    def __init__(self):
        self.name = None
        self.age = None

    # 用注解 @classmethod 修饰的方法就是类函数,可以用类名直接调用
    # 相当于Java中 static 修饰的类
    # 类一级中不能用实例的方法
    # cls 自动补充
    @classmethod
    def eat(cls):
        print("猫嗷嗷吃东西,嗷嗷吃")

    def aoao(self):
        Cat.eat()
        print("猫吃完饭为啥嗷嗷叫？")


# 使用类名直接调用类方法
Cat.eat()

# 在对象方法中调用类方法
cat = Cat()
cat.aoao()
