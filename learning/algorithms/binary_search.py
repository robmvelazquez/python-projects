"""
This function returns the index position of the target if found, else returns None.
Binary search divides the search space by 2 repeatedly until the target value is found or determined to be absent.
This function has a Big O value of O(log n) and the running time is Logarithmic
The list or array MUST be sorted in a sequential, ascending order for a successful binary search.
"""


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2  # floor division operator; divides by and rounds down to nearest whole number.

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


# This function verifies if the element was found and prints the index the element was found.
def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list.')


# This variable defines the elements within the list 'numbers'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 6)
verify(result)
