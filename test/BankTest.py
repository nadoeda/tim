import unittest


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def testEquality(self):
        list = generateBanknote(10, 100)
        self.assertEquals(self.bank.equality(list), True)

    def testAddCustomer(self):
        self.bank.addCustomer(0)
        self.assertIn(0, self.bank.listCustomer)

    def testSignRepository(self):
        self.bank.signRepository(self.bank.repository)
        self.assertTrue(all(banknote.signature != 0 for banknote in self.bank.repository.listBanknote))

    def testSignatureRecv(self):
        banknote = Banknote(0, 100)
        self.assertFalse(self.bank.recv(banknote, 0))

    def testRepeatRecv(self):
        self.bank.signRepository(self.bank.repository)
        banknote = self.bank.repository.listBanknote[1]
        self.assertFalse(self.bank.recv(banknote, 0))

    def testRecv(self):
        customer = Customer(self.bank, 0)
        self.bank.addCustomer(0)
        banknote = Banknote(99, 1000)
        banknote.signature = self.bank.digitalSign.sign(banknote)
        self.assertTrue(self.bank.recv(banknote, 0))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
