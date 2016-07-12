"""
Merge Sort
----------

Time Complexity: O(nlogn)

Space Complexity: O(n)

Stable: Yes

"""

def merge(left, right):
    """
    Takes two sorted lists and merges them into a single sorted list, then returns it.

    Args:
        left (arr): A list of sorted integers
        right (arr): A list of sorted integers

    Returns:
        arr: A list of sorted integers
    """
    i = 0
    j = 0
    n1 = len(A1)
    A = [0] * (len(left) + len(right))
    left.append('inf')
    right.append('inf')

    for k in xrange(len(A)):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else: 
            A[k] = right[j]
            j += 1
    return A

def merge_sort(A):
    """
    Takes a list of integers and sorts them in ascending order, then returns it.

    Args:
        A (arr): A list of integers

    Returns:
        arr: A list of sorted integers
    """
    if len(A) <= 1:
        return A
    middle = len(A)/2
    left = A[:middle]
    right = A[middle:]

    left = merge_sogit adrt(left)
    right = merge_sort(right)
    B = merge(left,right)
    return B
