import unittest


class TestRepository(TestCase):
    def setUp(self):
        self.repository = Repository()

    def testAdd(self):
        testBanknote = Banknote(1,100)
        self.repository.add(testBanknote)
        self.assertEquals(self.repository.listBanknote[0], testBanknote)

    def testRemove(self):
        testBanknote = Banknote(1, 100)
        self.repository.add(testBanknote)
        self.repository.remove(testBanknote)
        self.assertEquals(self.repository.listBanknote, [])

    def testCount(self):
        testBanknote1 = Banknote(1, 100)
        testBanknote2 = Banknote(2, 100)
        self.repository.add(testBanknote1)
        self.repository.add(testBanknote2)
        self.assertEquals(self.repository.count(100), 2)
        testBanknote3 = Banknote(2, 200)
        self.repository.add(testBanknote3)
        self.assertNotEquals(self.repository.count(100), 3)

    def testCountSignature(self):
        testBanknote1 = Banknote(1, 100, 1)
        testBanknote2 = Banknote(2, 100, 2)
        self.repository.add(testBanknote1)
        self.repository.add(testBanknote2)
        self.assertEquals(self.repository.countSignature(2), 1)
        testBanknote3 = Banknote(2, 200, 2)
        self.repository.add(testBanknote3)
        self.assertNotEquals(self.repository.count(2), 2)

    def testInitRepository(self):
        self.repository.initRepository(1200)
        self.assertEquals([self.repository.listBanknote[0].ratings,
                           self.repository.listBanknote[1].ratings,
                           self.repository.listBanknote[2].ratings], [1000, 100, 100])

    def testgetBanknoteRatings(self):
        testBanknote1 = Banknote(1, 1000, 1)
        testBanknote2 = Banknote(2, 100, 2)
        self.repository.add(testBanknote1)
        self.repository.add(testBanknote2)
        self.assertEquals(self.repository.getBanknoteRatings(100), testBanknote2)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
