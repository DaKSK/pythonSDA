from exceptions import Empty

class LinkedList:
	class Node(object):
		def __init__(self, element, next):
			self.element = element
			self.next = next

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def add_first(self, item):  # Puts at the beginning of list
		newest = self.Node(item, None)  # Create a newest node
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			newest.next = self.head
		self.head = newest
		self.size += 1

	def add_last(self, item):
		newest = self.Node(item, None)
		if self.is_empty():
			self.head = newest
			self.tail = newest
		else:
			self.tail.next = newest
		self.tail = newest
		self.size += 1

	def remove_first(self):
		if self.is_empty():
			raise Empty("Linked list is empty")
		value = self.head.element
		self.head = self.head.next
		self.size -= 1
		if self.is_empty():
			self.tail = None
		return value

	def remove_last(self):
		if self.is_empty():
			raise Empty("Linked list is empty")
		seeker = self.head
		i = 0
		print("length of self is", len(self))
		while i < len(self) - 2:
			seeker = seeker.next
			i += 1
		self.tail = seeker
		value = seeker.element
		self.tail.next = None
		self.size -= 1
		return value

	def display(self):  # Show elements of linked list
		seeker = self.head
		while seeker:
			print(seeker.element, end="-->")
			seeker = seeker.next # move seeker to next node
		print()  # new line


linked_list = LinkedList()
linked_list.add_first(10)
linked_list.add_first(30)
linked_list.display()
linked_list.remove_last()
linked_list.display()
