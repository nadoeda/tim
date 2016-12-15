from Bank import *
from Customer import *
from Banknote import *

NUMBERSEND = 100


class Manager:
    def __init__(self):
        self.bank = Bank()
        self.listCustomer = []

    def addCustomer(self, id):
        customer = Customer(self.bank, id)
        self.bank.addCustomer(customer.id)
        self.listCustomer.append(customer)

    def sendBanknoteCustomer(self, id, ratings):
        customer = self.listCustomer[id]
        banknote = customer.haveBanknote(ratings)
        if (banknote == 0):
            print('Error - banknote with input ratings not exist')
        else:
            if (self.bank.digitalSign.verify(banknote) == 0):
                print('Error - signature is not authentic')
            else:
                if (self.bank.repository.countSignature(banknote.signature) != 0):
                    print('Error - repeat use banknote')
                else:
                    self.bank.repository.add(banknote)
                    self.bank.listAccount[id].increase(ratings)
                    self.bank.listAccount[id].write()
                    self.bank.repository.writeCountRepository()
                    self.listCustomer[id].decrease(ratings)
                    customer.write()

    def getBanknoteCustomer(self, id, ratings):
        customer = self.listCustomer[id]
        list = generateBanknote(ratings, NUMBERSEND)
        list1 = customer.digitalSign.signListBanknote(list)
        list2 = self.bank.digitalSign.signListBanknote(list1[:(NUMBERSEND - self.bank.risk)])
        list3 = customer.digitalSign.removeSignListBanknote(list2)
        list2 = self.bank.digitalSign.removeSignListBanknote(list3)
        if (self.bank.equality(list2) == 0):
            print('Error - ratings is not equally')
        else:
            banknote = self.bank.digitalSign.sign(list[-1])
            self.bank.listAccount[id].decrease(ratings)
            self.bank.listAccount[id].write()
            self.listCustomer[id].repository.add(banknote)
            self.listCustomer[id].increase(ratings)
            self.listCustomer[id].write()
