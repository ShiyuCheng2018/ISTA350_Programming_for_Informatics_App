"""
Linked Lists and While Loops

A Node object will always evaluate to 
True when used as a Boolean expression.
Therefore, if node.next is pointing at a
Node object, node.next will evaluate to True
when used as a condition.

There is no terminal node on the list.  The
list just ends when a node with next == None
is reached.
"""

class Node:
    def __init__(self, datum=None):
        self.datum = datum
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        """
        Returns linked list as a regular list.
        Can be used to print what's in your linked list use for debugging!
        """
        lst = []
        current = self.head
        while current:
            lst.append(current.datum)
            current = current.next
        return lst

    #Implement the methods below

    def append(self, datum):
        """
        This method appends a new node to the end of your linked list
        with datum as its datum.
        If there's nothing in the linked list (self.head = None), set the
        head to the new node and return.
        """
        if self.head == None:
            self.head = Node(datum)
        else:
            current = self.head
            while current:
                pre = current
                current = current.next
            pre.next = Node(datum)

        return self.head

    def remove(self, datum):
        """
        Remove the first occurrence of element x from the list.
        If it isn't in the list, raise the ValueError with message
        'list.remove(x): x not in list'
        """
        current = self.head

        if current.datum == datum:
            self.head = current.next
            return self.head

        while current:
            if current.datum != datum:
                pre = current
                current = current.next

            else:

                pre.next = current.next
                return self.head

        return f'list.remove({datum}): {datum} not in list'



    def insert(self, i, datum):
        """
        Insert a new node at position i with datum as its datum.
        If i >= len(list), insert at the end.
        """
        current = self.head
        if i >= len(self.to_list()):
            self.append(datum)
            return self.head

        if i == 0:
            pre = current
            if current.next:
                current = current.next
                pre = Node(datum)
                pre.next = current
                print(pre.datum, current)
            else:
                self.append(datum)
            return self.head

        else:

            loop = 0
            while loop == i-1:
                pre = current
                current = current.next
                loop += 1

            pre.next = Node(datum)
            pre.next.next = current.next



    def pop(self, i = None):
        """
        Remove the node at position i and return its datum.
        If the list is empty, raise an IndexError with the message
        'pop from empty list'.  If i >= len(list), raise an 
        IndexError with the message 'pop index out of range'.
        """
        pass




