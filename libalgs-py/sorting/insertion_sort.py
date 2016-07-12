"""
Insertion Sort
--------------
Builds the sorted array by inserting one at a time.

Time Complexity: O(n^2)

Space Complexity: O(n)

Stable: Yes

"""

def insertion_sort(A):
	"""
	Takes a list of integers and sorts them in ascending order, then returns it.

	Args:
		A (arr): A list of integers

	Returns:
		arr: A list of sorted integers
	"""
	for i in xrange(1, len(A)):
		x = A[i]
		j = i-1
		while j >= 0 and A[j] > x:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = x
	return A
