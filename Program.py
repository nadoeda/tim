from Manager import *

man = Manager()
man.addCustomer(0)
print("Customer send 1000")
man.sendBanknoteCustomer(0, 1000)
print("Customer recv 500")
man.getBanknoteCustomer(0, 500)
