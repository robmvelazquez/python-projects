"""
Merge sort is a divide and conquer algorithm that sorts a list in ascending order
by finding the midpoint of a list and dividing into sub-lists. Returns a new sorted list.
Takes quasilinear O(n log n) time and linear O(n) space.
"""


def merge_sort(list):
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


# Divides unsorted list at midpoint into sub-lists and return two sub-lists: left and right. O(log n) logarithmic time.
def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


# Merge and sorts two lists (arrays), returns a new merged list. Overall O(n) linear time.
def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


# Recursive
def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


nums = [23, 75, 63, 35, 12, 59, 93, 26, 94]
l = merge_sort(nums)
print(verify_sorted(nums))
print(verify_sorted(l))
print(merge_sort(l))