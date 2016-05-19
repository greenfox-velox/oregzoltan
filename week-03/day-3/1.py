# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return self.radius*2*3.14159265

    def get_area(self):
        return self.radius**2*3.14159265

circ = Circle(10)
print("Circumference: ", circ.get_circumference())
print("Area: ", circ.get_area())
