from Account import *
from DigitalSignature import *
from Repository import *

STARTSUM = 1500
RISK = 99


class Bank:
    def __init__(self):
        self.listAccount = []
        self.listCustomer = []
        self.digitalSign = DigitalSignature()
        self.risk = RISK
        self.repository = Repository()

    def equality(self, list):  # возвращает 1 - если номиналы купюр равны
        ratings = list[0].ratings
        all([banknote.ratings != ratings for banknote in list])

    def addCustomer(self, customerId):
        self.listCustomer.append(customerId)
        account = Account(customerId, STARTSUM)
        self.listAccount.append(account)
        for list in self.listAccount:
            print(list.write())
        self.repository.initRepository(STARTSUM)
        self.signRepository(self.repository)
        self.repository.writeCountRepository()

    def signRepository(self, repository):
        for banknote in repository.listBanknote:
            banknote.signature = self.digitalSign.sign(banknote)

    def recv(self, banknote, id):
        if (self.digitalSign.verify(banknote) == False):
            print('Error - signature is not authentic')
            return False
        else:
            if (self.repository.countSignature(banknote.signature) != 0):
                print('Error - repeat use banknote')
                return False
            else:
                self.repository.add(banknote)
                self.listAccount[id].increase(banknote.ratings)
                self.listAccount[id].write()
                self.repository.writeCountRepository()
                return True

