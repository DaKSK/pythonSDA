'''
# Task 2
# 1- Read the CSV content from the file
# 2- Build a list of Students objects
# 3- Overwirte the __str__ method in the Student class to return the student data
#    formatted properly (name, age and scholarship)
# 4- Show all students

'''

import csv
from classes import Student

student_obj_list = []
with open("students.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        student = Student(row[0], row[1], row[2])
        student_obj_list.append(student)


print("The objects in the file are:")
print(student_obj_list)
print("\nHere's the contents:")
for item in student_obj_list:
    print(item)
