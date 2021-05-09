'''
1 - Lets improve our solution (phone book) that currently is storing, removing and searching contacts.
a. Create a class that represents a contact with fields (name, number and city);
b. Create a method that returns a string formatted for the contact, "Name - Number - City"
c. Create two properties, first_name and last_name. You should return the proper data for each one using the name (full name) field stored.
d*. Use a class to instanciate a contact based on values that the user typed and store it into the file.
e*. Use the class to build a list of contacts (objects from Contact class) and iterate over that.
2- Use the json third module for storing/retrieve data to/from the file. The methods dumps and loads will be useful for that.
'''
from os import path
import json


class Contact:

    def __init__(self, name, number, city):
        self.name = name
        self.number = number
        self.city = city

    def give_contacts(self):
        return f"{self.name} - {self.number} - {self.city}"

    @property
    def first_name(self):
        names = self.name.split(" ")
        return names[0]

    @property
    def last_name(self):
        names = self.name.split(" ")
        return names[-1]


def read_file(filepath):
    with open(filepath) as f:
        file_str = f.readline()
    print("File read")
    return file_str


def write_file(data, filepath):
    with open(filepath, "w") as f:
        f.write(str(data))
        print(f"Data has been saved to {filepath}")


def user_input():
    inserted_name = input("Name to add? ")
    inserted_number = input(f"Number to add to {inserted_name}? ")
    inserted_city = input(f"City to add to {inserted_name}? ")
    return inserted_name, inserted_number, inserted_city


filepath = "contact_book.json"
if not path.exists(filepath):
    write_file("[]", filepath)
'''
# INPUT FROM USER
name, number, city = user_input()
# CLASS OBJECT INITIALIZE
contact_class_instance = Contact(name, number, city)
# READ FILE IN
json_str_in = read_file(filepath)
# CONVERT FILE STRING INTO OBJECT
file_data = json.loads(json_str_in)
# ADD USER DATA TO (file.data) LIST IN DICTIONARY FORMAT(__dict__)
file_data.append(contact_class_instance.__dict__)
# UNPACK LIST OF INSTANCES TO JSON STRING WRITE ALL DATA TO FILE
json_str = json.dumps([contact_instance for contact_instance in file_data])
write_file(json_str, filepath)
# READ IN AND PRINT OUT
# json_str_in = read_file(filepath)
# file_data = json.loads(json_str_in)
# print(file_data)

# SEARCH for contact
type_to_search = input("Please specify: name, city or number")
thing_to_search = input(f"Write the {type_to_search}")
for contact_dict in file_data:
    if thing_to_search in contact_dict[type_to_search.lower()]:
        print("contact with", type_to_search, thing_to_search, "matched")
        print(contact_dict)

# DELETE
type_to_delete = "name"
thing_to_delete = input(f"Write the {type_to_delete}")
for contact_dict in file_data:
    if thing_to_delete in contact_dict[type_to_delete.lower()]:
        del contact_dict
        print(f"Deleted details of {thing_to_delete}")
        break

# READ IN new file data
print(file_data)
json_str = json.dumps([contact_instance for contact_instance in file_data])
# WRITE TO FILE data without the deleted element
write_file(json_str, filepath)
'''
run = True
while run is True:
    user_choice = input("Would you like to (a)dd, (s)earch, (d)elete or (q)uit your phonebook?")
    chosen_option = user_choice.lower()
    if "a" in chosen_option:
        name, number, city = user_input()
        contact_class_instance = Contact(name, number, city)

        json_str_in = read_file(filepath)
        file_data = json.loads(json_str_in)

        file_data.append(contact_class_instance.__dict__)

        json_str = json.dumps([contact_instance for contact_instance in file_data])
        write_file(json_str, filepath)
    elif "s" in chosen_option:
        type_to_search = input("Please specify: name, city or number")
        thing_to_search = input(f"Write the {type_to_search}")

        json_str_in = read_file(filepath)
        file_data = json.loads(json_str_in)

        for contact_dict in file_data:
            if thing_to_search in contact_dict[type_to_search.lower()]:
                print(contact_dict["name"], "-",  contact_dict["number"])

    elif "d" in chosen_option:
        type_to_delete = "name"
        thing_to_delete = input(f"Write the {type_to_delete}")

        json_str_in = read_file(filepath)
        file_data = json.loads(json_str_in)

        for contact_dict in file_data:
            if thing_to_delete in contact_dict[type_to_delete.lower()]:
                file_data.remove(contact_dict)
                print(f"Deleted details of {thing_to_delete}")

        json_str = json.dumps([contact_instance for contact_instance in file_data])
        write_file(json_str, filepath)
    elif "q" in chosen_option:
        print("Okay, exiting")
        run = False
