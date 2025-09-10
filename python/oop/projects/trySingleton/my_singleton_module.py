
# 1. Using the __new__ method:

"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # You can add initialization logic here if needed, but __init__ is usually preferred for object setup.
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # Output: True

"""

# 2. Using a Decorator:

""" 

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

# Usage
m1 = MyClass(10)
m2 = MyClass(20)

print(m1 is m2) # Output: True
print(m1.value) # Output: 10 (Note: __init__ is called only once for the first instance)

"""

#3. Module-level Singleton:

# my_singleton_module.py
class MyService:
    def __init__(self):
        self.data = "Shared Data"

service_instance = MyService() # This instance is created once when the module is imported

