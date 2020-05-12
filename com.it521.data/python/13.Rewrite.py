# 重写

class Animal:

    def eat(self):
        print("吃东西")


class Cat(Animal):

    def eat(self):
        print("猫吃东西")


cat = Cat()
# 在子类中可以定义与父类相同的名称的方法,此时子类的方法对父类的方法构成了重写
# 如果子类重写了父类的方法,使用子类对象调用被重写的方法时,执行子类中重写后的方法
cat.eat()
