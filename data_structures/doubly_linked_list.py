from exceptions import TooFew


class Node:
	def __init__(self, element, next=None, previous=None):
		self.element = element
		self.next = next
		self.previous = previous

	def __str__(self):
		prev_string = "<-->" if self.previous else ""
		next_string = f"{self.next}" if self.next else ""
		return f"{prev_string} {self.element} {next_string}"


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
		self.tail = None

	def get_size(self):
		seeker = self.head
		counter = 0
		while seeker:
			counter += 1
			seeker = seeker.next
		return counter

	def append(self, item):
		if self.head is None:
			newest = Node(item)
			self.head = newest
			self.tail = newest
			self.size += 1
		else:
			newest = Node(item)
			current = self.head
			while current.next:
				current = current.next
			current.next = newest  # Changing the last node pointer from None to new node
			newest.previous = current  # Changing the new node previous pointer to current selection
			newest.next = None
			self.tail = newest
			self.size += 1

	def prepend(self, item):
		if self.head is None:
			newest = Node(item)
			self.head = newest
			self.tail = newest
			self.size += 1
		else:
			newest = Node(item)
			self.head.previous = newest
			newest.next = self.head
			self.head = newest
			newest.previous = None
			self.size += 1

	def squeeze_in_after(self, this, after_that):
		if self.get_size() < 1:
			raise TooFew("Not enough nodes to squeeze after, try .append/.prepend first")
		else:
			new_node = Node(this)
			seeker = self.head
			while seeker:
				if seeker.element == after_that:
					new_node.next = seeker.next
					seeker.next.previous = new_node
					seeker.next = new_node
					new_node.previous = seeker
					self.size += 1
				seeker = seeker.next

	def display(self, rev=False):
		seeker = self.head
		back_seek = self.tail
		if not rev:
			while seeker:
				print(f"<--{seeker.element}", end="->")
				seeker = seeker.next  # move seeker to next node
		elif rev:
			while back_seek:
				print(f"<--{back_seek.element}", end="->")
				back_seek = back_seek.previous
		print()

	def print_list(self):
		return print(str(self.head))

	def return_penultimate(self):
		return self.tail.previous

	def extend_with_list(self, extension):
		for item in extension:
			self.append(item)

	def extend_with_llist(self, llist):
		seeker = llist.head
		while seeker:
			self.append(seeker.element)
			seeker = seeker.next


d_link_list = DoublyLinkedList()
d_link_list2 = DoublyLinkedList()
d_link_list.append(10)
d_link_list.append(20)
d_link_list.append(30)
d_link_list2.append(40)
d_link_list2.append(50)
d_link_list2.append(60)
d_link_list.extend_with_llist(d_link_list2)
d_link_list.print_list()
# d_link_list.print_list()
print("Size of DL-list is", d_link_list.get_size())
