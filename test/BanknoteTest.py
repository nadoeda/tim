
import unittest


class TestBanknote(unittest.TestCase):
    def setUp(self):
        self.banknote = Banknote(1, 5000, 0)

    def testBanknoteStr(self):
        str = ('id = ', 1, 'ratings = ', 5000)
        self.assertEquals(self.banknote.__str__(), str)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
