class Account:
    def __init__(self, id, sum):
        self.id = id
        self.sum = sum

    def increase(self, num):
        try:
            if num > 0:
                self.sum = self.sum + num
        except BaseException:
            raise ('Error - nominal is not korrect')

    def decrease(self, num):
        try:
            if num > 0 and self.sum > num:
                self.sum = self.sum - num
        except BaseException:
            raise('Error - nominal is not korrect')

    def write(self):
        print('account in bank: id =', self.id, ' sum = ', self.sum)
