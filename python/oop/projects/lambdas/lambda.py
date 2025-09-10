# lambdas in an array as element.

my_list = ['test_string', 99, lambda x : x ** 2]

print(my_list[2])
print(my_list[2](4))
print(my_list[2])

# lambdas passed to another function as callback

def invoker(callback):
    print(callback(6))

invoker(lambda y: 2 * y)
invoker(lambda xx: 2 + xx)

# stored in variable

add10 = lambda x : x+10
print(add10(3))
y = 34
print(add10(y))

# returned by another function 
def incrumanter(number):
    #start = number
    #some other logic code... or smth
    return lambda x: number - x

print(incrumanter(3))

print("------------------------------------\n")

# Lambdas & Other Functions

def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers_map = map(square, numbers)

print(squared_numbers_map) # Output: <map object at 0x...>

# Convert to a list to view the results
squared_numbers_list = list(squared_numbers_map)
print(squared_numbers_list) # Output: [1, 4, 9, 16]

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)  # Output: [1, 4, 9, 16, 25]

print("------sort() -  the sorted()----------\n")

# trying sort() -  the sorted() function and the .sort() method for lists.
# Using a built-in function as key
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers) # Default ascending sort
print(f"Default sorted numbers: {sorted_numbers}")

strings = ['apple', 'banana', 'kiwi', 'orange']
sorted_by_length = sorted(strings, key=len) # Sort by string length
print(f"Sorted by length: {sorted_by_length}")

# Using a custom defined function as key
def get_second_element(item):
    return item[1]

list_of_tuples = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_by_second_element = sorted(list_of_tuples, key=get_second_element)
print(f"Sorted by second element: {sorted_by_second_element}")

print("\n\n\n\n")

# Using a lambda function as key
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_descending = sorted(numbers, key=lambda x: -x) # Sort in descending order
print(f"Sorted descending with lambda: {sorted_descending}")

strings = ['apple', 'banana', 'kiwi', 'orange']
sorted_by_last_char = sorted(strings, key=lambda s: s[-1]) # Sort by the last character
print(f"Sorted by last character: {sorted_by_last_char}")

list_of_dictionaries = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted_by_age = sorted(list_of_dictionaries, key=lambda d: d['age']) # Sort by dictionary value
print(f"Sorted by age: {sorted_by_age}")

print("---->>> reduce python function------------\n")

# reduce python function with and without lambda function

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce with a lambda to sum the numbers
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum using lambda: {sum_result}")

# Using reduce with a lambda to find the product of the numbers
product_result = reduce(lambda x, y: x * y, numbers)
print(f"Product using lambda: {product_result}")

print("\n\n\n\n")

#from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

# Using reduce with a named function
def add_numbers(x, y):
    return x + y

sum_result_named = reduce(add_numbers, numbers)
print(f"Sum using named function: {sum_result_named}")

# Using reduce with a function from the operator module
product_result_operator = reduce(operator.mul, numbers)
print(f"Product using operator.mul: {product_result_operator}")

print("------------------------------------\n")

# all of the filter, map, sort, and reduce is immutable 