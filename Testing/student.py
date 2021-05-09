class Student:

    def __init__(self, name, age, grade=None):
        self.name = name
        self.age = age
        self.grade = grade

    def is_approved(self):
        return self.grade >= 7