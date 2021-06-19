import re

email = input("Type your email: ")

email_pattern = "[a-zA-Z\d]*\.?[a-zA-Z\d]*@[a-zA-Z\d]*\.[a-zA-Z\d]{2,3}"

is_email = re.fullmatch(email_pattern, email)
if is_email is not None:
	is_email = True
else:
	is_email = False

print(is_email)
