
import unittest


class TestExchange(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.customer = Customer(self.bank, 0)
        self.bank.addCustomer(0)
        self.exchange = Exchange(self.bank, self.customer, 100)

    def testExchange(self):
        self.assertTrue(self.exchange.exchange())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
