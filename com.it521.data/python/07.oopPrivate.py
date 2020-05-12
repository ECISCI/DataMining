# 封装
class Card:

    def __init__(self):
        self.card_id = None
        # 加上双下划线代表私有 相当于我们Java的Private
        self.__password = None

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password


card = Card()
card.setPassword("000000")
password = card.getPassword()
print(password)
