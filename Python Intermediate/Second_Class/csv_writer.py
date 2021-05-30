import csv

with open("employees.csv", 'a', newline="") as out_file:
	writer = csv.writer(out_file)
	writer.writerow(["Anna Dylan", 250])
