import random


class Banknote:
    def __init__(self, id, ratings, signature=0):
        self.id = id
        self.ratings = ratings
        self.signature = signature

    def __str__(self):
        return ('id = ', self.id, 'ratings = ', self.ratings)


def generateBanknote(ratings, num):  # возвращает лист банкнот количества num и заданным номиналом
    return [Banknote(random.randint(100, 1000), ratings) for _ in range(num)]
