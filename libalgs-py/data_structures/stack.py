"""
Stack
-----
A LIFO abstract data type that serves as a collection of elements.

"""

class Stack(object):

	def __init__(self):
		"""
		Attributes:
			data (arr): data stored in the stack
		"""
		self.data = []

	def empty(self):
		"""
		Returns whether or not the stack is empty.

		Time Complexity: O(1)
		
		Returns:
			bool: whether or not the stack is empty
		"""
		return len(self.data) == 0

	def push(self, x):
		"""
		Pushes an element onto the stack.

		Time Complexity: O(1)

		Args:
			x: item to be added
		"""
		self.data.append(x)

	def pop(self):
		"""
		Pops an element off the stack. 

		Time Complexity: O(1)

		Returns:
			any: the last element on the stack

		"""
		return self.data.pop()

	def peek(self):
		"""
		Returns the last item on the stack but doesn't remove it.

		Time Complexity: O(1)

		"""
		return self.data[-1]
