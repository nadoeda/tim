from Bank import *
from DigitalSignature import *
from Banknote import *

STARTSUM = 2100


class Customer:
    def __init__(self, bank, id):
        self.bank = bank
        self.digitalSign = DigitalSignature()
        self.id = id
        self.sum = STARTSUM
        self.write()

        self.repository = Repository()
        self.repository.initRepository(STARTSUM)
        self.bank.signRepository(self.repository)
        self.repository.writeCountRepository()

    def increase(self, num):
        try:
            if num > 0:
                self.sum = self.sum + num
        except BaseException:
            raise ('Error - nominal is not korrect')

    def decrease(self, num):
        try:
            if num > 0 and self.sum > num:
                self.sum = self.sum - num
        except BaseException:
            raise ('Error - nominal is not korrect')

    def write(self):
        print('customer: id =', self.id, ' sum = ', self.sum)

    def haveBanknote(self, ratings):
        return self.repository.count(ratings)

    def getBanknote(self, ratings):  # возвращает купюру с заданным номиналом
        return self.repository.getBanknoteRatings(ratings)

    def send(self, ratings):
        try:
            if (self.haveBanknote(ratings)):
                banknote = self.getBanknote(ratings)
                try:
                    if (self.bank.recv(banknote, self.id)):
                        self.decrease(banknote.ratings)
                        self.write()
                        self.repository.writeCountRepository()
                        return True
                except BaseException:
                    raise ('Error - Send banknote customer')
        except BaseException:
            raise ('Error - don\'t have banknote')
