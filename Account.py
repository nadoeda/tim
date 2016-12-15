class Account:
    def __init__(self, id, sum):
        self.id = id
        self.sum = sum

    def increase(self, num):
        self.sum = self.sum + num

    def decrease(self, num):
        self.sum = self.sum - num

    def write(self):
        print('account in bank: id =', self.id, ' sum = ', self.sum)
