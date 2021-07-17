class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def find_sum(self, root):
		if root.value is None:
			return 0
		return root.value + root.find_sum(root.left) + root.find_sum(root.right)
