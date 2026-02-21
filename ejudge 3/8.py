class Account:
    def __init__(self, balance,withdrawal):
        self.balance=balance
        self.withdrawal=withdrawal
    def withdraw(self):
        if self.balance>self.withdrawal:
            self.balance-=self.withdrawal
            return self.balance
        elif self.balance==self.withdrawal:
            self.balance-=self.withdrawal
            return 0
        else:
            return "Insufficient funds"
    
balance,withdrawal=map(int,input().split())
account=Account(balance,withdrawal)
print(account.withdraw())