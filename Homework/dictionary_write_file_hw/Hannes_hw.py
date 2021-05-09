def writer():
	while True:
		PhoneList = []
		name = input("Enter your name:\nTo cancel, type 'q'")  # lets you write your name
		if not name.isalpha():
			print("Please enter a valid name!")
			continue
		if name == 'q':  # If user writes "q" after asking for name it will close the program
			exit()
		number = input("Enter your phone nr: \n")  # lets you write phone nr
		if not number.isnumeric():  # Checks if person used numbers
			print("Phone number cant contain letters!")
			break
		city = input("Enter the City: \n")
		if not city.isalpha():
			print("Please enter a valid city name!")
		else:
			PhoneList.append(
				"You have added: Name: " + name + " - Phone Number: " + number + " - City: " + city + " to the phonebook!")
			print(PhoneList)  # Shows you the info you have added to the PhoneList on the code
			with open("phonebook.txt", "a+") as f:
				f.seek(0)
				data = f.read(100)
				if len(data) > 0:
					f.write("\n")
				f.writelines(PhoneList)
				print("The info has been saved to phonebook.txt")
			f.close()  # Closes the phonebook.txt
			print("Would you like to add more contacts?")
			print("'Yes' - 'No'")
			query = input(" ")
			if query == "Yes":
				print("\n")
				continue
			elif query == "No":
				print("\n")
				main()


def search():
	print("Who would you like to search for?")
	user = input(" ")
	with open("phonebook.txt") as f:
		for line in f:
			if user in line:
				print("Here the contact:")
				print(line)
				search()
			else:
				print("This name does not exist!\n")
				main()


def delete():
	print("Who would you like to erase?")
	user = input(" ")
	with open("phonebook.txt") as f:
		for line in f:
			if user in line:
				line = f.readline()
				with open("phonebook.txt", "w") as fn:
					for lines in line:
						if line.strip("\n") != lines:
							fn.write(line)
							f = open("phonebook.txt")
							print("Here are the remaining contacts!:")
							print(line)
							print(" ")
							main()


def show():
	count = 0
	print("\nHere are all the contacts:")
	with open("phonebook.txt") as f:
		lines = f.readlines()
		for line in lines:
			count += 1
			print("Line{}: {}".format(count, line.strip()))
			print(" ")
		main()


def main():
	print("What would you like to do?")
	print("Add - Find - Delete - Show - Exit")
	query = input(" ")
	if query == "Add":
		writer()
	elif query == "Find":
		search()
	elif query == "Delete":
		delete()
	elif query == "Show":
		show()
	elif query == "Exit":
		print("have a great day!")
		exit()


main()