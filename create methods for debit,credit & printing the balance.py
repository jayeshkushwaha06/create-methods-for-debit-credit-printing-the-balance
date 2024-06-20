class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no =acc
acc1 = Account(10000,12345)  
print(acc1.balance)
print(acc1.account_no)