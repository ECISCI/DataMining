class Father:

    def sing(self):
        print("唱歌好听")

    def dance(self):
        print("跳舞难看")

    pass


class Mother:
    def sing(self):
        print("唱歌难听")

    def dance(self):
        print("跳舞好看")

    pass


# 如果存在方法冲突,调用括号中的Father因为Father在第一位
class Child(Father, Mother):

    def sing(self):
        Father.sing(self)
        Mother.sing(self)
        print("我特么哪里知道？")


child = Child()
child.sing()

print(Child.__mro__)
# child.dance()
