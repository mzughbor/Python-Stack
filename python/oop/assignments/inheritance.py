class BankAccount():

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

    def receive_money(self, amount):
        self.balance += amount
        return self


class RetirementAccount(BankAccount):

    def __init__(self, int_rate, balance=0, is_roth):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth


class CheckingAccount(BankAccount):

    def receive_money(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().receive_money()
        return self


