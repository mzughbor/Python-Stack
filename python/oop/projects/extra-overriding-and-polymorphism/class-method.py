class Employee:
    raise_percentage = 1.05  # class-level attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage  # affects all employees
        # cls means class >> 
        # Always use cls as the first parameter name in classmethods to clearly 
        # indicate that the method works with the class, not instances.

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))  # alternative constructor

# Example usage
emp1 = Employee("Alice", 5000)
emp2 = Employee.from_string("Bob-6000")  # Created using @classmethod

print(emp1.raise_percentage)
print(emp2.raise_percentage)

print("---\n")

print(emp1.salary)  # 5000
print(emp2.salary)  # 6000

print("---\n")


emp1.set_raise_percentage(1.555)
#Employee.set_raise_percentage(1.555)
# weather was using any em* or Employee as class name
# about calling or execuation..

print("---\n")
print(emp1.raise_percentage)
print(emp2.raise_percentage)


