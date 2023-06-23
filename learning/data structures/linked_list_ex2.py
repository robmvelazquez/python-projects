"""
Linked lists do not have index positions.
An object for storing a single node of a linked list. Models data and the next node in the list.
L/L are used for dynamic memory allocation, stack and queue, 'undo' functionality, hash tables,
and graphs.
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

if __name__ == '__main__'

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
