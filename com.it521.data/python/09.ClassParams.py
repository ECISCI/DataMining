# 类变量
class Cat:
    # 全局的就是类变量
    # 类似于Java 中 public static final String = ""
    # 此处没有Java中的final修饰,这个值可以更改
    subject = "猫科"

    def __init__(self):
        self.__name = None
        # 加上双下划线代表私有 相当于我们Java的Private
        self.__age = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


cat = Cat()
# 对象的属性设置值
cat.setName("张三猫")
cat.setAge(12)
# 打印对象属性值
print(cat.getName())
print(cat.getAge())

# 打印原有类变量值
print(Cat.subject)

# 更改类变量的值
Cat.subject = "山狸猫"
print(Cat.subject)

# 类变量直接取值 相当于我们Java中的静态
