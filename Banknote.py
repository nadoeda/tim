import random


class Banknote:
    def __init__(self, id, ratings, signature=0):
        self.id = id
        self.ratings = ratings
        self.signature = signature

    def write(self):
        print('id = ', self.id, 'ratings = ', self.ratings)  # 'signature = ', self.signature)


def generateBanknote(ratings, num):  # возвращает лист банкнот количества num и заданным номиналом
    list = []
    i = 0
    while (i < num):
        list.append(Banknote(random.randint(100, 1000), ratings))
        i = i + 1
    return list
