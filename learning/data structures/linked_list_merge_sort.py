from linked_list import LinkedList

"""
Sorts a linked list in ascending order.
- Recursively divides linked list into sub-lists containing a single node.
- Repeatedly merge the sub-lists to produce sorted sub-lists until one remains.
- Returns a sorted linked list.
"""


# Runs in O(kn log n)
def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


# Divide unsorted list at midpoint into sub-linked-lists. Takes O(k log n) time.
def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

# Merges and sorts two linked lists by data in the nodes, returning a new, merged list.
def merge(left, right):
    # Create a new linked list that contains nodes from merging left and right. Runs in linear O(n) time.
    merged = LinkedList()

    # Add a fake head that is discarded later.
    merged.add(0)

    # Set current to the head of the linked list.
    current = merged.head

    # Obtain head nodes for left and right linked lists.
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until the tail node is reached.
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the tail node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node, obtain node data to perform comparison operations/
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    return merged


l = LinkedList()
l.add(14)
l.add(74)
l.add(2)
l.add(56)
l.add(27)
l.add(72)
l.add(13)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)