class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship


p2 = Person("Jane", 32)
s2 = Student(p2.name, p2.age, 300)
p1 = Person("Henry", 54)
print(p1)
s1 = Student("Jack", 34, 1000)
print(s1)
e1 = Employee("Johnson", 22, 14.5, 20)
print(e1)
ws1 = WorkingStudent("Peter", 23, 10.7, 25, 500)
print(ws1)
