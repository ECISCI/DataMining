# init方法的使用
class Dog:

    # init方法是在创建对象的时候被运行,无需手工调用即可执行
    # 对于程序中声明,定义的方法在特定的时机自动执行的方法,叫魔术方法
    def __init__(self):
        self.type = "波斯狗"
        self.age = 2
        self.name = None
