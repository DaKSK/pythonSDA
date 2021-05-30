"""
1- Create a program read from users (name, age)
2- In case of user type a blank name raise a ValueError exception
3- Create your own custom exception (AgeLimitException) and raise that if the user is less than 18
Bonus: If error raised return to ask again
"""


class AgeLimitException(Exception):
    def __init__(self):
        message = "Please check the age (<18)"
        super().__init__(message)


name = input("Name please")
if name == "":
    raise ValueError("Need to name it something, please write a name")

while True:
    try:
        age = input("Age please")
        if int(age) < 18:
            raise AgeLimitException
    except AgeLimitException as e:
        print(e)
        continue
    break
