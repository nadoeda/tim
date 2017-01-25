import unittest


class TestDigitalSignature(unittest.TestCase):
    def setUp(self):
        self.digitalSignature = DigitalSignature()

    def testGetPrivateKey(self):
        self.assertEquals(self.digitalSignature.getPrivateKey(), self.digitalSignature.privateKey)

    def testGetPublicKey(self):
        self.assertEquals(self.digitalSignature.getPublicKey(), self.digitalSignature.publicKey)

    def testSign(self):
        banknote = Banknote(123, 500)
        self.assertNotEqual(self.digitalSignature.sign(banknote), 0)
        self.assertEqual(self.digitalSignature.verify(banknote), 0)

    def testVerify(self):
        banknote = Banknote(123, 500)
        banknote.signature = self.digitalSignature.sign(banknote)
        self.assertTrue(self.digitalSignature.verify(banknote))
        banknote2 = Banknote(125, 500)
        self.assertEquals(self.digitalSignature.verify(banknote2), 0)

    def testEncryptDecrypt(self):
        banknote = Banknote(123, 500)
        message = self.digitalSignature.encrypt(banknote)
        self.assertEqual(self.digitalSignature.decrypt(banknote, message), str([banknote.id, banknote.ratings]).encode('utf-8'))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()