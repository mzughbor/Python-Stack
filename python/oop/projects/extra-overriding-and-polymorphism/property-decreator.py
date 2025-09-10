class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height  # calculated when accessed

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage
rect = Rectangle(4, 5)
print(rect.area)      # 20 (no parentheses!)
print(rect.perimeter) # 18


print("////////////////////////////////////\n")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius of the circle."""
        print("hi, I do return it..")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("hi, there!")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Radius must be a non-negative number.")
        self._radius = value

    @property
    def area(self):
        """Calculates the area of the circle."""
        return 3.14159 * (self._radius ** 2)

# Usage
my_circle = Circle(5)
print(my_circle.radius)  # Accesses the getter: 5
print(my_circle.area)    # Accesses the computed property: 78.53975

print("---\n")
#my_circle.radius = 7     # Calls the setter
#print(my_circle.radius)  # 7

""" 
try:
    my_circle.radius = -2
except ValueError as e:
    print(e)  # Radius must be a non-negative number. """