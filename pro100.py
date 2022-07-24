class atm(object):
    def _init_(self, atmCardNo, atmPinNo, balance, amount, left):
        self.atmCardNo=atmCardNo
        self.atmPinNo= atmPinNo
        self.balance=balance
        self.amount=amount
        self.left=left
    def cashWithdrawal(self):
        return self.amount
    def balanceEnquiry(self):
        return self.left

ansruta=atm("1", "2", "20000", "1200", "18800")
print(ansruta.cashWithdrawal())
print(ansruta.balanceEnquiry())