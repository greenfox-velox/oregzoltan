# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():
    def __init__(self):
        self.total = 0
        self.i = 0

    def add_grade(self, grade):
        self.grade = grade
        self.total += grade
        self.i += 1

    def get_average(self):
        return self.total / self.i

janika = Student()
janika.add_grade(2)
janika.add_grade(1)
janika.add_grade(5)
janika.add_grade(2)
print(janika.get_average())
