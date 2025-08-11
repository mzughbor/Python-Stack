#the methods don’t rely on instance or class data  
#Use @staticmethod for utility functions that belong conceptually to a class but don’t 
#need instance or class data.
#It’s mostly about code organization and clarity.


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @staticmethod
    def validate_isbn(isbn):
        # Dummy example: ISBN must be 13 characters
        return isinstance(isbn, str) and len(isbn) == 13

# Usage:
print(Book.validate_isbn("1234567890123"))  # True
print(Book.validate_isbn("invalidisbn"))    # False

print("---\n")
print("---\n")



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9/5 * c + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

print(TemperatureConverter.celsius_to_fahrenheit(0))   # 32.0
print(TemperatureConverter.fahrenheit_to_celsius(32))  # 0.0
