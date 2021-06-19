import re

two_name_pattern = "[A-Z][a-z]+\s[A-Z][a-z]+"
text = "Aecio Costa is a Software developer, John Doe is his friend. His sister call Maria Julia"

list_of_names = re.findall(two_name_pattern, text)
print("names found in text:", list_of_names)
result = False
name_to_check = input("Write the name to check: ")
if name_to_check in list_of_names:
	result = True
print(result)
