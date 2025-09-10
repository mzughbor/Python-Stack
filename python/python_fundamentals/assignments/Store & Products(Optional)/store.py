import product

class Store:
    def __init__(self, name, list_of_products=[]):
        self.name = name
        self.products = list_of_products
    
    def add_product(self, new_product, price, category):
        new_product = product.Product(new_product, price, category)
        self.products.append(new_product)
        return self

    #sell_product(self, id) - remove the product from the store's list of products given the id 
    # (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):
        
        for i, product in enumerate(self.products): # enumerate track of the index as i

            if product.id == id:
                sold_product = self.products.pop(i)
                print("Sold Product Info:")
                sold_product.print_info()
                return
        print("Sorry, Product not found.")

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

    def show_products(self):
        for product in self.products:
            product.print_info()
