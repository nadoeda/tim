from Bank import *
from Customer import *


class Manager:
    def __init__(self):
        self.bank = Bank()
        self.listCustomer = []

    def addCustomer(self, id):
        customer = Customer(self.bank, id)
        self.bank.addCustomer(customer.id)
        self.listCustomer.append(customer)
