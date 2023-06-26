"""
Circular linked list - the last node maintains the address of the first node to establish a circular
connection via circular linked list. In circular doubly linked list, the first node also maintains
the address of the last node. Insertion can occur at any three positions within the list.
T/S Complexity:
  Insertion Time = O(1) if operation does not require traversal, O(n) if required
  Insertion Space = O(1)
  Deletion T/S = O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        # Allocate memory to the new node and add data to the node
        newNode = Node(data)

        # Assign last to newNode
        self.last = newNode

        # Create link to itself
        self.last.next = self.last
        return self.last

    # Add node to the front
    def addFront(self, data):

        # Check if the list is empty
        if self.last == None:
            return self.addToEmpty(data)

        # Allocate memory to the new node and add data to the node
        newNode = Node(data)

        # Store the address of the current first node in the newNode
        newNode.next = self.last.next

        # Make newNode as last
        self.last.next = newNode

        return self.last

    # Add node to the end
    def addEnd(self, data):
        # Check if the node is empty
        if self.last == None:
            return self.addToEmpty(data)

        # Allocate memory to the new node and add data to the node
        newNode = Node(data)

        # Store the address of the last node to the next of newNode
        newNode.next = self.last.next

        # Point the current last node to the newNode
        self.last.next = newNode

        return self.last

    # Insert node after a specific node
    def addAfter(self, data, item):

        # Check if the list is empty
        if self.last == None:
            return None

        newNode = Node(data)
        p = self.last.next
        while p:

            # If the item is found, place newNode after it
            if p.data == item:

                # Make the next of the current node as the next of newNode
                newNode.next = p.next

                # Put newNode to the next of p
                p.next = newNode

                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

      # Delete a node
      def deleteNode(self, last, key):

          # If linked list is empty
          if last == None:
              return

          # If the list contains only a single node
          if (last).data == key and (last).next == last:

              last = None

          temp = last
          d = None

          # If last node is to be deleted
          if (last).data == key:

              # Find the node before the last node
              while temp.next != last:
                  temp = temp.next

              # Point temp node to the next of last
              temp.next = (last).next
              last = temp.next

          # Travel to the node to be deleted
          while temp.next != last and temp.next.data != key:
              temp = temp.next

          # If node to be deleted was found
          if temp.next.data == key:
              d = temp.next
              temp.next = d.next

          return last

    def traverse(self):
        if self.last == None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
          print(newNode.data, end=" ")
          newNode = newNode.next
          if newNode == self.last.next:
              break

# Driver code
if __name__ == "__main__":

    cll = CircularLinkedList()

    last = cll.addToEmpty(6)
    last = cll.addEnd(8)
    last = cll.addFront(2)
    last = cll.addAfter(10, 2)

    cll.traverse()

    last = cll.deleteNode(last, 8)
    print()
    cll.traverse()
  
