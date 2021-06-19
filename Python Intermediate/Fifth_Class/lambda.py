# result = lambda x: str(x + "3")
# print(result("i"))

# List comprehensions
numbers = []
for number in range(1, 317):
    numbers.append(number)

odd_list = [i for i in numbers if i % 2 != 0]
print("The length of our generated odds list")
print(len(odd_list))

squared_list = [i**2 for i in numbers]
print("List comprehended squares of values")
print(squared_list[0:10])

# Lambda expressions

# Let's try to use the lambda with map to square the values of a list
values_to_square = [1, 2, 3, 4, 5, 6, 7]

squared_map = map(lambda x: x**2, values_to_square)
print("Mapped squared values with lambda:")
print(list(squared_map))

fruits = ["apples", "bananas", "lemons"]
capital_fruits = map(lambda x: x.upper(), fruits)
print(list(capital_fruits))