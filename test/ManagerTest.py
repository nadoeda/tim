import unittest


class TestManager(unittest.TestCase):
    def setUp(self):
        self.man = Manager()


    def testAddCustomer(self):
        customer = Customer(self.man.bank, 0)
        self.man.addCustomer(0)
        self.assertEquals(self.man.listCustomer[0].id, customer.id)


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
