# writer.py
# Ask the user for name/phonenumber/city
# Store his/her data into a file using this format:
'''
{'aecio': {'phonenumber':'5435345', 'city':'Tallinn'},'sebastian': {'phonenumber':'5345345', 'city':'Parnu'}}
'''

# INPUT and WRITE

name = input("What's your name?")
phone_number = input("What's your phone?")
city = input("What's your city?")

# To put the inner dictionary in the outer we need to create inner first
inner_dictionary_1 = {"phonenumber": phone_number, "city": city}
outer_dictionary = {name: inner_dictionary_1}

print(outer_dictionary)

# READ in the file as it is.
with open("file.txt") as f:
    file_content_str = f.readline()   # read lines method makes a list of file content

if file_content_str == "":
    file_content_str = "{}"

outer_dictionary = eval(file_content_str)
outer_dictionary[name] = inner_dictionary_1
# WRITE
with open("file.txt", "w") as f:    # Switching to write mode
    f.write(str(outer_dictionary))     # taking the list version of our content and writing it in
    print("Data has been saved to file.txt")
