# Task 1
# 1- Ask the user to type name, age, rate and num_of_hours
# 2- Create a new instance of Employee(name, age, rate, num_of_hours)
# 3- Create a method (as_json(self)) to represent a employee in JSON format
# 4- Save the employee into the json file

# Task 2
# 1- Read the JSON content from the file
# 2- Build a list of Employee objects
# 3- Overwrite the __str__ method in the Employee class to return the employee data
#    formatted properly (name, age, rate, num_of_hours and finance)
# 4- Show all employees

import json
from classes import Employee

employee_name = input("Employee name ")
age_yr = int(input("Employee age "))
rate = float(input("Hourly rate "))
num_of_hours = int(input("Working hours"))

employee = Employee(employee_name, age_yr, rate, num_of_hours)

list_of_employees = []
with open("employees.json") as f:
	list_of_employees = json.load(f)

list_of_employees.append(employee.as_json())

with open("employees.json", "w") as f:
	json.dump(list_of_employees, f)

list_of_employees_objects = []
for member in list_of_employees:
	employee = Employee(member["name"], member["age"], member["rate"], member["number of hours"])
	list_of_employees_objects.append(employee)

print("Employees in file:")
for employee_data in list_of_employees_objects:
	print(employee_data.name)
