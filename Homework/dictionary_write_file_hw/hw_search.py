# search.py
# SEARCH and display on console
# Ask the user a name and shows his/her data in case of this user has been found
name_to_search = input("Search - Please input username : ")

with open("file.txt") as f:
    file_content_str = f.readline()   # read lines method makes a list of file content

if file_content_str == "":
    file_content_str = "{}"

outer_dictionary = eval(file_content_str)

if name_to_search in outer_dictionary:
    print("Data found: ", outer_dictionary.get(name_to_search))
else:
    print("No such user found")