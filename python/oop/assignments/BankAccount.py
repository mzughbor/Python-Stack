class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print("Balance is:", self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


account1 = BankAccount(0.01)
account1.deposit(50).withdraw(75).yield_interest().display_account_info()

print("\n")

account2 = BankAccount(0.02, 50)
account2.deposit(50)
account2.withdraw(75)
account2.yield_interest()
account2.display_account_info()

print("\n")

account3 = BankAccount(0, 500)
account3.withdraw(499)
account3.withdraw(75)
account3.yield_interest()
account3.display_account_info()
