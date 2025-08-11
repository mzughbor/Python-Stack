#Polymorphism 

#ex - remote control - DVD player, TV channels, playStastion ... Same interface → different behavior.

# Parent class
class Account:
    def __init__(self, balance):
        self.balance = balance

    # Operator overloading: adding two accounts
    def __add__(self, other):
        if isinstance(other, Account):
            return Account(self.balance + other.balance)
        else:
            raise TypeError("Can only add Account to Account")

    # Method meant to be overridden
    def account_type(self):
        pass
        #raise NotImplementedError("Subclasses must define account_type()")
        return "Generic Account"


# Subclass 1: Savings account
class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"


# Subclass 2: Checking account
class CheckingAccount(Account):
    def account_type(self):
        return "Checking Account"


# ---- DEMO ----

# Create two accounts
acc1 = SavingsAccount(1000)
acc2 = CheckingAccount(500)

# Operator overloading example
merged_acc = acc1 + acc2
print(f"Merged balance: {merged_acc.balance}")  # Merged balance: 1500

# Method overriding + polymorphism example
for acc in [acc1, acc2, merged_acc]:
    print(acc.account_type())
