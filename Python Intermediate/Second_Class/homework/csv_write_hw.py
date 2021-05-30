import csv


class Student:
	def __init__(self, name, age, scholarship):
		self.name = name
		self.age = age
		self.scholarship = scholarship

	def to_csv(self):
		return [self.name, self.age, self.scholarship]


student_name = input("Student name ")
age_yr = int(input("Student age "))
scholarship_eur = input("Scholarship amount ")

student = Student(student_name, age_yr, scholarship_eur)

print(student.to_csv())
with open("students.csv", 'a', newline="") as out_file:
	writer = csv.writer(out_file)
	writer.writerow([i for i in student.to_csv()])
