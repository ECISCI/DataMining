# 多态 父类指针指向自己的子类对象

class Animal:
    def eat(self):
        print("吃东西")


class Driver:

    def driver(self):
        print("开车")


class Cat(Animal, Driver):

    def eat(self):
        print("猫吃东西")

    def driver(self):
        print("猫开车")


class Test:

    def play(self, driver):
        driver.driver()


# 方法一 创建一个司机
driver = Driver()
# 方法二 创建了一个具有司机特征的对象
cat = Cat()

test = Test()
test.play(driver)
test.play(cat)
