"""
This function returns the index position of the target if found, else returns None.
In the worst-case scenario, the for loop search through the entire range of values and read every element within the
list, which equates to a Big O value of 'n', or (O(n))
"""


# This function will utilize a linear search to sequentially find a specific element within a list or array.
def linear_search(list, target):
    for index in range(0, len(list)):
        if list[index] == target:
            return index
    return None


# This function verifies if the element was found and prints the index the element was found.
def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list.')


# This variable defines the elements within the list 'numbers'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 6)
verify(result)