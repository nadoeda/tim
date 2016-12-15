from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from Banknote import *


class DigitalSignature:
    def __init__(self):
        self.privateKey = RSA.generate(1024)
        self.publicKey = self.privateKey.publickey()

    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.getPublicKey()

    def sign(self, banknote):  # возвращает подпись банкноты
        message = str([banknote.id, banknote.ratings]).encode('utf-8')
        key = RSA.importKey(bytes(self.privateKey.exportKey('PEM')))
        h = SHA256.new(message)
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(h)
        return signature

    def verify(self, banknote):  # возвращает 1 - если подпись верна, иначе - 0
        signature = bytes(banknote.signature)
        message = str([banknote.id, banknote.ratings]).encode('utf-8')
        key = RSA.importKey(bytes(self.publicKey.exportKey('PEM')))
        h = SHA256.new(message)
        verifier = PKCS1_v1_5.new(key)
        if verifier.verify(h, signature):
            return 1
        else:
            return 0

    def encrypt(self, bancnote):  # возвращает подпись клиента
        message = str([bancnote.id, bancnote.ratings]).encode('utf-8')
        crypto = self.publicKey.encrypt(message, 111)
        return crypto

    def decrypt(self, bancnote, crypto):  # снять подпись клиента
        message = self.privateKey.decrypt(crypto)
        return message

    def signListBanknote(self, list):  # возвращает лист купюр подписанный клиентом
        for banknote in list:
            banknote.ratings = self.encrypt(banknote)
        return list

    def removeSignListBanknote(self, list):  # возвращает лист купюр не подписанный клиентом
        for banknote in list:
            banknote.ratings = self.decrypt(banknote, banknote.ratings)
        return list

    '''def removeSign(self, banknote):'''
