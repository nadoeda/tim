from Banknote import *
import random


class Repository():
    def __init__(self):
        self.listBanknote = []

    def add(self, banknote):
        self.listBanknote.append(banknote)

    def remove(self, banknote):
        self.listBanknote.remove(banknote)

    def count(self, ratings):  # возврвщвет количество купюр с заданным номиналом
        n = 0
        for list in self.listBanknote:
            if list.ratings == ratings:
                n = n + 1
        return n

    def countSignature(self, signature):  # возврвщвет количество купюр с заданной подписью
        n = 0
        for list in self.listBanknote:
            if list.signature == signature:
                n = n + 1
        return n

    def write(self):
        for list in self.listBanknote:
            list.write()

    def writeCountRepository(self):
        print('5000 - ', self.count(5000))
        print('1000 - ', self.count(1000))
        print('500 - ', self.count(500))
        print('100 - ', self.count(100))

    def initRepository(self, sum):
        while sum >= 5000:
            self.add(Banknote(random.randint(1, 100), 5000))
            sum = sum - 5000
        while sum >= 1000:
            self.add(Banknote(random.randint(1, 100), 1000))
            sum = sum - 1000
        while sum >= 500:
            self.add(Banknote(random.randint(1, 100), 500))
            sum = sum - 500
        while sum >= 100:
            self.add(Banknote(random.randint(1, 100), 100))
            sum = sum - 100

    def getBanknoteRatings(self, ratings):  # возвращает банкноту с заданным номиналом
        banknote = ''
        for list in self.listBanknote:
            if list.ratings == ratings:
                banknote = list
                self.listBanknote.remove(list)
                break
        return banknote
