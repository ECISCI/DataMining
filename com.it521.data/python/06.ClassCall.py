# 类的成员方法调用成员属性

class Dog:

    def __init__(self):
        self.type = "波斯狗"
        self.age = 2
        self.name = None

    # 自报家门
    def introdeuce(self):
        self.catch()
        print("我是一只 %s 我的名字叫 %s 颜色 %s" % (self.type, self.name, self.color))

    def __str__(self):
        return "卧槽"

    def catch(self):
        print("抓猫")


dog = Dog()
dog.name = "大帅"
# 独有属性存在一定的风险
dog.color = "黄狗"
print(dog.introdeuce())

### 类里面出现的self相当于我们Java里的this指针 相当于当前类的对象
