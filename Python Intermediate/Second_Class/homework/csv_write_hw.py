import csv
from classes import Student

student_name = input("Student name ")
age_yr = int(input("Student age "))
scholarship_eur = float(input("Scholarship amount "))

student = Student(student_name, age_yr, scholarship_eur)

with open("students.csv", 'a', newline="") as out_file:
	writer = csv.writer(out_file)
	writer.writerow(student.to_csv().split(","))
