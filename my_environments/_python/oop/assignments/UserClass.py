class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}"
            
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("We are sorry, Not sufficient balance")
        return self

    def display_user_balance(self):
        print("User:", self.name, ", Balance:", self.balance)
        return self
    
    def receive_money(self, amount):
        self.balance += amount
        return self

    def transfer_money(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.receive_money(amount)
            print(f"Transfering money to user {other_user}, is completed.")
        else:
            print("We are sorry, Not sufficient balance to transfer.")
        return self

user1 = User("Mahmoud")
user1.make_deposit(50).make_deposit(100).make_deposit(20).make_withdrawal(50).display_user_balance()

user2 = User("Soha")
user2.make_deposit(500).make_deposit(100).make_withdrawal(200).make_withdrawal(170).display_user_balance()

user3 = User("Ali")
user3.make_deposit(100).make_withdrawal(120).make_withdrawal(10).make_withdrawal(17).display_user_balance()

user1.transfer_money(user3,50)
user1.display_user_balance()
user3.display_user_balance()