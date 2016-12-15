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
        self.sum = self.sum + num

    def decrease(self, num):
        self.sum = self.sum - num

    def write(self):
        print('customer: id =', self.id, ' sum = ', self.sum)

    def haveBanknote(self, ratings):  # возвращает купюру с заданным номиналом, 0 - если нет таких купюр
        if self.repository.count(ratings) != 0:
            return self.repository.getBanknoteRatings(ratings)
        else:
            return 0
