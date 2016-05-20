# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)

    def salute(self):
        total = 0
        self.greet()
        for each in self.grades:
            total += each
        print("Average of grades: ", total/len(self.grades))

someone = Person("Bela", "Nagy")
someone.greet()
someone2 = Student("Lajos", "Kis")
someone2.add_grades(2)
someone2.add_grades(3)
someone2.add_grades(2)
someone2.add_grades(3)
someone2.salute()
