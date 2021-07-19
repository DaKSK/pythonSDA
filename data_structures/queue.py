from exceptions import Empty


class Queue:
	def __init__(self):
		self.queue = []
		self.front = 0
		self.size = 0

	def enqueue(self, v):
		self.queue.append(v)
		self.size += 1

	def dequeue(self):
		if self.is_empty() is True:
			raise Empty("Queue is empty")
		value = self.queue[self.front]  # create a variable which will be assigned the element of the 0th index
		self.queue.remove(value)  # remove the value or set the element at the front index equal to none
		self.front = self.front + 1  # Increment the front index
		self.size -= 1
		return value
		# return self.queue.pop(0)

	def __len__(self):
		return len(self.queue)  # Set the len to be equal to size, to get the correct size but with None values in the queue

	def is_empty(self):
		return self.queue == []


q = Queue()
print("The queue is empty -", q.is_empty())
q.enqueue("first")
q.enqueue("second")
print(f"queue: {q.queue}")
print(f"queue size_ {q.__len__()}")
print(q.dequeue())
print(f"Queue:", q.queue)
q.enqueue("third")
q.enqueue("fourth")
print(f"queue size_ {q.__len__()}")
print(q.queue)
