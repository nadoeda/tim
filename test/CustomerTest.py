import unittest


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.customer = Customer(self.bank, 0)

    def testEncrease(self):
        testBalance1 = 2115
        testBalance2 = 5079
        self.customer.increase(15)
        self.assertEqual(self.customer.sum, testBalance1)
        self.assertNotEqual(self.customer.sum, testBalance2)
        self.assertRaises(BaseException, self.customer.increase(-30))

    def testDecrease(self):
        testBalance1 = 2000
        testBalance2 = 4999
        self.customer.decrease(100)
        self.assertEqual(self.customer.sum, testBalance1)
        self.assertNotEqual(self.customer.sum, testBalance2)
        self.assertRaises(BaseException, self.customer.decrease(-5000))

    def testHaveBanknote(self):
        banknote = Banknote(11, 100)
        self.customer.repository.add(banknote)
        self.assertEquals(self.customer.haveBanknote(banknote), 0)

    def textGetBanknote(self):
        banknote = Banknote(11, 5000)
        self.customer.repository.add(banknote)
        banknote2 = self.customer.getBanknote(5000)
        self.assertEquals(banknote, banknote2)

    def testSend(self):
        self.assertRaises(BaseException, self.customer.send(200))
        banknote = Banknote(11, 500)
        self.customer.repository.add(banknote)
        self.assertRaises(BaseException, self.customer.send(500))
        self.bank.addCustomer(0)
        self.assertTrue(self.customer.send(100))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
