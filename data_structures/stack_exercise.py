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


def is_matching_brackets(string):
	stack = Stack()
	openers = "({["
	for symbol in string:
		if symbol in openers:
			stack.push(symbol)
		else:		# If symbol is not an opener, it's a closer
			if not stack.items:
				return False		# If stack is empty we can't have matches
			other_symbol = stack.pop()		# Assuming the closer is correct we pop, but save to check
			if other_symbol == "(":		# Checking case of (
				if symbol != ")":
					return False		# False because we closed "(" with something other than ")"
			elif other_symbol == "[":		# Checking case of [
				if symbol != "]":
					return False		# False because we closed "[" with something other than "]"
			elif other_symbol == "{":		# Checking case of {
				if symbol != "}":
					return False		# False because we closed "{" with something other than "}"
	if not stack.items:
		return True
	else:
		return False


if __name__ == "__main__":
	sequence_string = "[{()()()}{([])}{}[()()()]]"
	print(is_matching_brackets(sequence_string))
