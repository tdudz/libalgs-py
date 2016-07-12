"""
Bogo Sort
---------
Picks two elements at random and swaps them until sorted.

Time Complexity: O((n+1)!)

Space Complexity: O(1)

Stable: No

"""

from random import shuffle

def is_sorted(A):
	"""
	Takes a list of integers and checks if it is sorted in ascending order.

	Args:
		A (arr): A list of integers

	Returns:
		bool: True if sorted, False otherwise
	"""
    for i in xrange(1,len(A)):
        if A[i] < A[i-1]:
            return False
    return True

def bogo_sort(A):
	"""
	Takes a list of integers and sorts them in ascending order, then returns it.

	Args:
		A (arr): A list of integers

	Returns:
		arr: A list of sorted integers
	"""
    while not is_sorted(A):
        shuffle(A)
    return A
