from exceptions import Empty


class LinkedList:
	# Node inside the Linked List class
	class Node(object):
		def __init__(self, element, next):
			self.element = element
			self.next = next

	# Linked list initialization
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	# Add a node to the beginning of the linked list
	def add_first(self, item):
		newest = self.Node(item, None)
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			newest.next = self.head
		self.head = newest
		self.size += 1

	# Add a node to the end of the linked list
	def add_last(self, item):
		newest = self.Node(item, None)
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			self.tail.next = newest
		self.tail = newest
		self.size += 1

	# Add a node between other nodes
	def between(self, item, left_side, right_side):
		if self.size < 2:
			raise Empty("The linked list has too few elements, can't add between")
		else:
			new_node = self.Node(item, None)
			seeker = self.head
			while seeker:
				if seeker.element == left_side and seeker.next.element == right_side:
					new_node.next = seeker.next
					seeker.next = new_node
				seeker = seeker.next
		self.size += 1

	# Remove the first node
	def remove_first(self):
		if self.is_empty():
			raise Empty("Linked list is empty")
		value = self.head.element
		self.head = self.head.next
		self.size -= 1
		if self.is_empty():
			self.tail = None
		return value

	# Remove the last node
	def remove_last(self):
		if self.is_empty():
			raise Empty("Linked list is empty")
		seeker = self.head
		i = 0
		while i < len(self) - 2:  # -2 Because we need to access the previous node pointer
			seeker = seeker.next
			i += 1
		self.tail = seeker
		value = seeker.element
		self.tail.next = None
		self.size -= 1
		return value

	# Show the whole linked list
	def display(self):  # Show elements of linked list
		seeker = self.head
		while seeker:
			print(seeker.element, end="-->")
			seeker = seeker.next  # move seeker to next node
		print()  # new line


linked_list = LinkedList()
linked_list.add_first(10)
linked_list.add_first(30)
linked_list.display()
linked_list.remove_last()
linked_list.display()
linked_list.add_first(10)
linked_list.between(20, 10, 30)
linked_list.between(25, 20, 30)
linked_list.display()
