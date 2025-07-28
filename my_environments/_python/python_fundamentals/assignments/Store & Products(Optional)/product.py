import random
import string

class Product:
    used_ids = set() # no duplications thats our need for now

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = self.generate_unique_id()

    def generate_unique_id(self):
        chars = string.ascii_letters + string.digits # '0123456789' + 'abcdefgh... with capitiels...
        while True:
            new_id = ''.join(random.choices(chars, k=8))
            if new_id not in Product.used_ids:
                Product.used_ids.add(new_id)
                return new_id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price +=  self.price * percent_change
        else:
            self.price -=  self.price * percent_change
        return self

    def print_info(self):
        print(f"Name is :{self.name}, Product ID: {self.id}, from Category of :{self.category}, Price ${self.price}")
        return self
