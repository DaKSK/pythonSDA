def read_file():
    with open('PHONEBOOK.txt') as file:
        data= file.readline()

    if data == '':
        data ='{}'
    getDict = eval(data)
    return getDict


outer_dict = read_file()
#  Function for checking numbers in inputs


def checkNumbers(data):
    for character in data:
        if character.isdigit():
            contains_digit = True
            return contains_digit


def write():
    while True:
        name = input('Name  : ').lower()
        if checkNumbers(name):
            print("IT should not contain numbers. Try again")
            continue
        if name == "":
            print("It should contain some data. Try again")
            continue
        else:
            break
    while True:
        try:
            nr   =  int(input('Number : '))
        except ValueError:
            print("Not a number. Insert only numbers please.")
            continue
        else:
            break
    while True:
        city = input('Location : ').lower()
        if checkNumbers(city):
            print("IT should not contain numbers. Try again")
            continue
        if city == "":
            print("It should contain some data. Try again")
            continue
        else:
            break

    inner_dict={
        'phonenumber' : nr,
        'city': city
    }
    outer_dict[name] = inner_dict

    with open('PHONEBOOK.txt', mode='w') as file:
        file.write(str(outer_dict) + "\n"  )
        print(f"Contact name '{name}' with number {nr} with {city} address has been added")


def search_name():
    name = input('Who are you looking for : ').lower()
    user_data = outer_dict.get(name)

    if user_data is None:
        print('This user is not in the book')
    else:
        print(f"{name} -\tnr:{user_data.get('phonenumber')} \n\t\taddress:{user_data.get('city')}")


def delete():
    name = input("Who would you like to discard from book : ")
    user_data = outer_dict.pop(name,None)

    if user_data is None:
        print("The user does not exist, try again!")
    else:
        with open('PHONEBOOK.txt', mode='w') as file:
            file.writelines(str(outer_dict))
        print(f"Contact {name} has been removed")

def loadPhoneBook():

    # First it is iterating through outer dictionary . On a second loop, it is iterating through inner dictionary  values
    # and getting its key and value pairs

    # get key and value pair from all dictionary
    for key,value in outer_dict.items():
        print('------')
        # key is same as name in this case
        print(f"{key} ")
        # get last key (means name) inner dictionary value {phonenumber: 3443,city: Tallinn} and seperate this again
        # for key and value pairs (now you can print phonenumber,without its number or
        # just print city name without its key value)
        for key, value in value.items():
            print(f"{key}:{value}")


def search_city():
    user_input = input("What city do you want to search for : ").lower()
    people_count = 0
    # just for names
    people_list =[]
    # list for strings
    people_data_list = []

    for name in outer_dict:
        user_data = outer_dict.get(name)

        for a,b in outer_dict[name].items():
            if a == 'city' and b == user_input:
                people_list.append(name)
                people_count += 1
                people_data_list.append(f"\n{name.capitalize()}, phonenumber : {user_data.get('phonenumber')}")
    print(f"{people_count} people ({people_list}) live in {user_input}. {''.join(people_data_list)}.")


def init():
    while True:
        user_input= input("Give a action (add/search/browse/delete/exit) : ").lower()
        actions =['add','search','delete','browse','exit']
        if user_input not in actions:
           print('Invalid Command!')
        if user_input == 'add':
            print("Ready to add contact")
            write()
        if user_input == 'search':
            while True:
                search_for= input("Do you want to search by person or by city (person/city) ? :")
                if search_for == 'person':
                    print("Ready to search for person")
                    search_name()
                    break
                if search_for == 'city':
                    print("Ready to search for city")
                    search_city()
                    break
                if search_for != 'person' or search_for != 'city':
                    continue

        if user_input == 'delete':
            print("Ready to delete")
            delete()
        if user_input == 'browse':
            loadPhoneBook()
        if user_input == 'exit':
             exit()

init()
