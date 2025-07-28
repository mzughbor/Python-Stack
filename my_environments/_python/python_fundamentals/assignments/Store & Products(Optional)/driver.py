# test our work

from store import Store

# Create store
my_store = Store("Mahmoud's Shop")

# Add products using your improved idea (method chaining!)
my_store.add_product("Laptop", 1000, "Electronics")\
        .add_product("T-Shirt", 20, "Clothing")\
        .add_product("Headphones", 100, "Electronics")

# Show initial products
print("\n-- Initial Products --")
my_store.show_products()

# Apply inflation
my_store.inflation(0.10)  # +10%
print("\n-- After Inflation --")
my_store.show_products()

# Apply clearance
my_store.set_clearance("Clothing", 0.50)  # -50%
print("\n-- After Clearance on Clothing --")
my_store.show_products()

# Sell one product (manually pick first ID for demo)
print("\n-- Selling Product --")
product_to_sell = my_store.products[0].id
my_store.sell_product(product_to_sell)

# Final list
print("\n-- Remaining Products --")
my_store.show_products()
