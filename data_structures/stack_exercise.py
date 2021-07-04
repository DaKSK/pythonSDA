class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


def matching_brackets(string, stack):
	for symbol in string:
		if symbol == "(":
			stack.push(symbol)
	for other_symbol in string:
		if other_symbol == ")":
			stack.pop()
	print(stack.items)
	if stack.is_empty():
		return True, "We have matching brackets"
	elif not stack.is_empty():
		return False, "We don't have matching brackets"
	else:
		return "Quantum state?"


brackets = "()"
sequence = Stack()

print(matching_brackets(brackets, sequence))

