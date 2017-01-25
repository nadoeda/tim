import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(1, 5000)

    def testAccountIncrease(self):
        testBalance1 = 5077
        testBalance2 = 5079
        self.account.increase(77)
        self.assertEqual(self.account.sum, testBalance1)
        self.assertNotEqual(self.account.sum, testBalance2)
        self.assertRaises(BaseException, self.account.increase(-30))

    def testAccountDecrease(self):
        testBalance1 = 4900
        testBalance2 = 4999
        self.account.decrease(100)
        self.assertEqual(self.account.sum, testBalance1)
        self.assertNotEqual(self.account.sum, testBalance2)
        self.assertRaises(BaseException, self.account.decrease(-5000))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
