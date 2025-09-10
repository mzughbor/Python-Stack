class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email, int_rate=0.0, account_balance=0):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, account_balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User:", self.name, "Balance:", self.account.balance)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self


user1 = User("Mahmoud", "mzughbor@gmail.com", 0.05, 500)
user1.make_deposit(100)
user1.make_withdrawal(300)
user1.display_user_balance()
user1.yield_interest()
user1.display_user_balance()