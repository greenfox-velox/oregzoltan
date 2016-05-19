# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grade = grade
        self.grades.append(grade)

    def get_average(self):
        total = 0
        for i in self.grades:
            total += i
        return total / len(self.grades)

janika = Student()
janika.add_grade(2)
janika.add_grade(3)
janika.add_grade(5)
janika.add_grade(2)
print(janika.get_average())
