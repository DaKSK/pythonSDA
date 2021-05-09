# DELETES the name from dictionary and file
# Works only on the information given in this session
# Does not work for data stored in the file from inactive sessions

name_to_delete = input("Delete - Please input username to delete : ")   # String of the name of user to delete

with open("file.txt") as f:
    file_content_str = f.readline()   # read lines method makes a list of file content

if file_content_str == "":
    file_content_str = "{}"

outer_dictionary = eval(file_content_str)

if name_to_delete in outer_dictionary:
    del outer_dictionary[name_to_delete]        # Delete the user key:value pair from dictionary
    with open("file.txt", "w") as f:            # open the file to write the changes to file
        f.writelines(str(outer_dictionary))     # Convert the dictionary to string and write the updated data
    print(name_to_delete, "has been deleted")   # Tell user job is done
else:
    print("No such user found, file unchanged")     # Tell user nothing happened
