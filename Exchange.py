from Banknote import *
from Bank import *
from Customer import *

NUMBERSEND = 100


class Exchange():
    def __init__(self, bank, customer, ratings):
        self.bank = bank
        self.customer = customer
        self.ratings = ratings
        self.id = customer.id
        # self.exchange()

    def exchange(self):
        list = generateBanknote(self.ratings, NUMBERSEND)
        list1 = self.customer.digitalSign.signListBanknote(list)
        list2 = self.bank.digitalSign.signListBanknote(list1[:(NUMBERSEND - self.bank.risk)])
        list3 = self.customer.digitalSign.removeSignListBanknote(list2)
        list2 = self.bank.digitalSign.removeSignListBanknote(list3)
        try:
            if not self.bank.equality(list2):
                banknote = list[-1]
                banknote.signature = self.bank.digitalSign.sign(banknote)
                banknote.ratings = self.ratings
                self.bank.listAccount[self.id].decrease(self.ratings)
                self.bank.listAccount[self.id].write()
                self.bank.repository.writeCountRepository()
                self.customer.repository.add(banknote)
                self.customer.increase(self.ratings)
                self.customer.write()
                self.customer.repository.writeCountRepository()
                return True
        except BaseException:
            raise ('Error - ratings is not equally')
