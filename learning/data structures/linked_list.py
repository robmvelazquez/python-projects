"""
Linked lists do not have index positions.
An object for storing a single node of a linked list. Models data and the next node in the list.
L/L are used for dynamic memory allocation, stack and queue, 'undo' functionality, hash tables,
and graphs.
"""


class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


# Singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    # Returns the number of nodes in the list, takes 0(n) time.
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    # Adds a new Node containing data at the head of the list. Takes O(n) time.
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Searches for the first node that contains data that matches the key. Returns node or None if not found. O(n) Time.
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    """
    Inserts a new Node containing data at index position. 
    Insertion takes 0(1) but finding node at insertion point
    takes 0(n) time. Overall, takes 0(n) time.
    """
    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    # Removes node containing data that matches the key. Returns the node or None if the key doesn't exist. Takes 0(n).
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    # Returns a string representation of the list, takes O(n) time.
    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)
