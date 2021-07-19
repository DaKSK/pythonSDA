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

	# Use static method in case function empty_stack should be grouped with class
	# @staticmethod
	# def empty_stack(stack):
	# 	while stack.is_empty() is not True:
	# 		print(stack.pop())


# Use a separate function empty_stack if function not grouped with class
# For more robust code, should check instance of class first before executing

def empty_stack(stack):
	assert isinstance(stack, Stack)
	while stack.is_empty() is not True:
		print(stack.pop())


history = Stack()
history.push("google.com")
history.pop()
history.push("yahoo.com")
history.push("amazon.com")

empty_stack(history)
print(history.is_empty())
