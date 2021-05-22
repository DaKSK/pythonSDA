"""
1- Create a program read from users (name, age)
2- In case of user type a blank name raise a ValueError exception
3- Create your own custom exception (AgeLimitException) and raise that if the user is less than 18
"""


class AgeLimitException(Exception):
    def __init__(self):
        message = "This person is too young, please check the age"
        super().__init__(message)


name = input("Name please")
if name == "":
    raise ValueError("Need to call you something, please write a name")
age = int(input("Age please"))
if age < 18:
    raise AgeLimitException


