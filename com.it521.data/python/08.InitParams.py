# init传参
class Card:

    def __init__(self, car_id, type):
        self.card_id = car_id
        # 加上双下划线代表私有 相当于我们Java的Private
        self.type = type


card = Card("09090","黑卡")

print(card.type)
print(card.card_id)
