from os import path

def user_data_to_dict(name, number, city):
    # To put the inner dictionary in the outer we need to create inner first
    inner_dictionary = {"phonenumber": number, "city": city}
    outer_dictionary = {name: inner_dictionary}
    return outer_dictionary, inner_dictionary


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
    name = input("Name to add? ")
    number = input(f"Number to add to {name}? ")
    city = input(f"City to add to {name}? ")
    return name, number, city


def replace_empty_string(file_string):
    if file_string == "":
        file_string = "{}"
        print("File was empty string, created empty dictionary")
        return file_string


def search_name(username):
    if username in outer_dictionary:
        print("Data found: ", outer_dictionary.get(username))
    else:
        print("No such user found")


def search_city(city_searched, dictionary):
    search_city_result = []
    for key_1, value1 in dictionary.items():
        for key_2, value2 in value1.items():
            if value2 == city_searched:
                phone_number = value1["phonenumber"]
                search_city_result.append(f"{key_1}, {phone_number}")
    return search_city_result


def delete_user(username):
    if username in outer_dictionary:
        del outer_dictionary[username]
        with open("file.txt", "w") as f:
            f.writelines(str(outer_dictionary))
        print(name_to_delete, "has been deleted")
    else:
        print("No such user found, file unchanged")


if not path.exists("file.txt"):
    write_file("{}", "file.txt")

run = True
while run is True:
    user_choice = input("Would you like to (a)dd, (s)earch, (d)elete or (q)uit your phonebook?")
    chosen_option = user_choice.lower()
    if "a" in chosen_option:
        name, number, city = user_input()
        outer_dictionary, inner_dictionary = user_data_to_dict(name, number, city)
        file_str = read_file("file.txt")
        replace_empty_string(file_str)
        outer_dictionary = eval(file_str)
        outer_dictionary[name] = inner_dictionary
        write_file(outer_dictionary, "file.txt")
    elif "s" in chosen_option:
        city_or_name = input("WAIT! CHOOSE first! Search By (c)ity or (n)ame? ")
        if "n" in city_or_name.lower():
            name_to_search = input("Now, input name to search: ")
            file_str = read_file("file.txt")
            replace_empty_string(file_str)
            outer_dictionary = eval(file_str)
            search_name(name_to_search)
        elif "c" in city_or_name.lower():
            city_to_search = input("Now input city to search by: ")
            file_str = read_file("file.txt")
            replace_empty_string(file_str)
            outer_dictionary = eval(file_str)
            search_result = search_city(city_to_search, outer_dictionary)
            search_amount = len(search_result)
            print(f"There are {search_amount} users in", city_to_search)
            print("\n".join(search_result))
        else:
            print("Please type either 'c' for city OR 'n' for name")
    elif "d" in chosen_option:
        name_to_delete = input("Delete - Please input username to delete : ")
        file_str = read_file("file.txt")
        replace_empty_string(file_str)
        outer_dictionary = eval(file_str)
        delete_user(name_to_delete)
    elif "q" in chosen_option:
        print("Okay, exiting")
        run = False
