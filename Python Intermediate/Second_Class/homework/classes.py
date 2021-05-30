class Student:
    def __init__(self, name, age, scholarship):
        self.name = name
        self.age = age
        self.scholarship = scholarship

    def to_csv(self):
        return f"{self.name}, {self.age}, {self.scholarship}"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.scholarship}"

    def __repr__(self):
        return f"{self.name} data"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_finance(self):
        pass

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours

    def as_json(self):
        return {"name": self.name, "age": self.age, "rate": self.rate, "number of hours": self.num_of_hours}

    def __str__(self):
        return f"{self.name}, {self.age}, {self.rate}, {self.num_of_hours}"


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour + self.scholarship
