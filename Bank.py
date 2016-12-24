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
        self.repository.initRepository(STARTSUM)

    def equality(self, list):  # возвращает 1 - если номиналы купюр равны
        ratings = list[0].ratings
        return all([banknote.ratings == ratings for banknote in list])

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
        try:
            if (self.digitalSign.verify(banknote)):
                try:
                    if (self.repository.countSignature(banknote.signature) == 0):
                        self.repository.add(banknote)
                        self.listAccount[id].increase(banknote.ratings)
                        self.listAccount[id].write()
                        self.repository.writeCountRepository()
                        return True
                except BaseException:
                    raise ('Error - repeat use banknote')
        except BaseException:
            raise ('Error - signature is not authentic')
