import re

pattern = '[a-zA-Z\d*]*\.[a-zA-Z\d*]*'
text = 'My user name is aecio.costa , please register me in the system'

result = re.search(pattern, text)

print(result)
print(result.start())
print(result.end())

print("Has been found", text[result.start():result.end()])
