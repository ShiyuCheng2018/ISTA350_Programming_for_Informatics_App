
#### ISTA 350 Midterm Review ####


### Matrices ###

def is_identity(matrix_lst):
    """
    This function takes one parameter, matrix_lst, which represents a list of 
    lists. 

    You will return true if the matrix_list is an identity matrix. Recall that 
    an identity matrix has ones along the main diagonal and zeros everywhere
    else. 

        Example:
            matrix_lst = [[1, 0, 0],
                          [0, 1, 0], 
                          [0, 0, 1]]

            Would result to True.
    """


def sum_diagonal(matrix_lst):
    """
    This function takes one parameter, matrix_lst, which represents a list of 
    lists. 

    You will return the sum of the main diagonal.

        Example:
            matrix_lst = [[5, 4, 0],
                          [1, 5, 6], 
                          [8, 2, 4]]

            would return 14
    """


"""
Practice with two's complement binary numbers.

Negate the following two's complement binary numbers.
What are the decimal equivalents of the original binary numbers?
101101: 
010101: 

"""


'''
Linked Data Structures

A Node object will always evaluate to 
True when used as a Boolean expression.
Therefore, if node.next is pointing at a
Node object, node.next will evaluate to True
when used as a condition.

There is no terminal node on the list.  The
list just ends when a node with next == None
is reached.
'''

# TO-DO: Implement Node __init__ and SortedLinkedList __init__, 
# insert, and remove methods.

class Node:
    def __init__(self, datum):
        '''
        The goal of this class is to instantiate an instance of a Node
        for a doubly linked list.
        This class should contain an instance variable named 'datum' and
        two pointer instance variables called 'previous' and 'next' that are 
        initialized to None.
        '''

class SortedLinkedList:
    '''
    This class should implement a sorted linked list.  It is a combination of a
    doubly linked list (pointers both directions in each Node) and a double-ended
    linked list (has pointers to both the beginning (head) and end (tail) of the 
    list.  The list should be maintained in sorted order at all 
    times.  Duplicates are allowed.
    '''
    def __init__(self, items=None):
        '''
        This class should contain an instance variable named head and an
        instance variable called tail that will point at the beginning and
        end Nodes of the list, respectively.  Initialize them to None.  insert 
        will take care of the inserting an item into an empty list.  items is 
        a list of data to be inserted into the list.  If there is anything in items,
        insert them into the list.
        '''

    def to_list(self):
        '''
        GIVEN

        This method creates a list from your linked list so it can be
        printed. USE THIS TO DEBUG YOUR CODE.
        '''
        lst = []
        current = self.head
        while current:
            lst.append(current.datum)
            current = current.next
        return lst

    def insert(self, datum):
        '''
        MUST WORK FOR THE TESTS OF THE REST OF THE METHODS TO WORK
        
        This method should insert items into your linked list in sorted order.
        You should maintain the order of the list (which should be sorted
        initially) 
        '''
    
    def remove(self, item):
        '''
        Remove an occurrence of item and return True or
        return False if item not in list.
        '''

### Binary ###
# TO-DO: Implement __mul__ method.

class Binary:
    '''
    GIVEN: THE ENTIRETY OF HW4.  YOU MAY USE ANY FUNCTIONALITY EXCEPT int 
    FROM HW4.  
    
    Open up your hw4 and code this up inside it so you can add a main and 
    test it.
    '''
    
    def __mul__(self, other):
        '''
        Implement instance magic method mul (short for multiply) for class Binary.
        It takes one Binary object as an argument.
        (Hint: 4 * 3 = 4 + 4 + 4) You should be able to complete this with the methods provided.
        You may assume that both instances (the multiplicand and the multiplier) represent
        nonnegative numbers.
        
        You may NOT use an decimal integers.  You may use any functionality that
        you coded up in hw4, except int.
        
        Do not alter either instance.
        '''

def main():
    '''
    Test your functions in main!  Tests for SortedLinkedList are provided.
    Uncomment them when you get to that part.
    '''
    """
    print('*' * 15, 'Testing Node', '*' * 15)
    
    n = Node(5)
    assert n.next is None
    assert n.previous is None
    assert n.datum == 5
    
    print('*' * 15, 'Node passes', '*' * 15)
    print('*' * 15, 'Testing SLL insert', '*' * 15)
    
    l = SortedLinkedList()
    assert l.head is None
    assert l.tail is None
    
    l = SortedLinkedList([99, -1, 3, -1, 2, 3, 99])
    print('Should be [-1, -1, 2, 3, 3, 99, 99]:', l.to_list())

    print('*' * 15, 'Testing SLL remove', '*' * 15)
    
    l = SortedLinkedList()
    assert not l.remove(5)

    l = SortedLinkedList([99, -1, 3, -1, 2, 3, 99, 4])
    print('Should be [-1, -1, 2, 3, 3, 4, 99, 99]:', l.to_list())

    assert not l.remove(5)
    assert l.remove(4)
    print('Should be [-1, -1, 2, 3, 3, 99, 99]:', l.to_list())
    assert l.remove(-1)
    print('Should be [-1, 2, 3, 3, 99, 99]:', l.to_list())
    assert l.remove(-1)
    print('Should be [2, 3, 3, 99, 99]:', l.to_list())
    assert l.remove(3)
    print('Should be [2, 3, 99, 99]:', l.to_list())
    assert l.remove(99)
    print('Should be [2, 3, 99]:', l.to_list())
    assert l.remove(99)
    print('Should be [2, 3]:', l.to_list())
    assert l.remove(2)
    print('Should be [3]:', l.to_list())
    assert l.remove(3)
    print('Should be []:', l.to_list())
    """

if __name__ == '__main__':
    main()
