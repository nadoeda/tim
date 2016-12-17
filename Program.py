from Manager import *
from Exchange import *

man = Manager()
man.addCustomer(0)
print("Customer send 1000")
man.listCustomer[0].send(1000)
print("Customer recv 500")
Exchange(man.bank, man.listCustomer[0],  500)
