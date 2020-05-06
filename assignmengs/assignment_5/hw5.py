"""
Author: Shiyu Cheng (23329948)
ISTA 350 Hw5
SL: Jacob Heller
Date: 4/1/20
Summary: This homework is the culmination of the first half of the course's content, incorporating linked data
structures, magic methods, and algorithms whose runtimes and big O's we will examine in class. You will be implementing
Node and BST classes.
"""


class Node:
    """
    initializes an instance variable called datum to the argument, and instance variables
    left and right to None
    """

    def __init__(self, arg):
        self.datum = arg
        self.left = self.right = None

    def __add__(self, item):
        """
        Insert a new item (this method's sole argument) into the subtree that has self as its root,
        if the item is not already in the tree.  Do this such that the rules of binary search trees
        are maintained (see Introduction) after insertion
        :param item: datum
        :return:
        """
        if (self.datum or self.left or self.right) == item:
            return
        if item < self.datum:
            if not self.left:
                self.left = Node(item)
            else:
                self.left + item
        else:
            if not self.right:
                self.right = Node(item)
            else:
                self.right + item

    def __contains__(self, item):
        """
        This magic method takes an item and returns True if the item is in the subtree that has self as its
        root, False otherwise.
        :param item: datum
        :return:
        """
        if self.datum == item:
            return True
        if self.left:
            if item in self.left:
                return True
        if self.right:
            if item in self.right:
                return True
        return False

    def __eq__(self, other):
        """
        Takes a Node object as an argument.  Return True if the subtrees that has self and other as their
        roots have the same shape and the corresponding Node objects have the same data
        :param other:
        :return:
        """
        if not other:
            return False
        if self.datum == other.datum and self.left == other.left and self.right == other.right:
            return True
        return False

    def sort(self, _list):
        """
        Takes a list and appends the data in the subtree that has selfas its root in sorted order
        :param list:list
        :return:
        """
        if self.left:
            self.left.sort(_list)
        _list.append(self.datum)
        if self.right:
            self.right.sort(_list)
        return _list


class BST:

    def __init__(self, arg=None):
        """
        init takes one argument with a default value of None.  If the argument is None,
        set self.root to None.  Otherwise, initialize self.root to a Node containing the argument
        :param arg:
        """
        if arg:
            self.root = Node(arg)
        else:
            self.root = None

    def __add__(self, item):
        """
        Insert a new item into self
        :param item:
        :return:
        """
        if self.root:
            if self.root.datum == item:
                return
            else:
                self.root + item
        else:
            self.root = Node(item)

    def __contains__(self, item):
        """
        This magic method takes an item and returns True if the item is in self, False otherwise.
        :param item:
        :return:
        """
        if self.root:
            if self.root.datum == item:
                return True
            if self.root.left:
                if item in self.root.left:
                    return True
            if self.root.right:
                if item in self.root.right:
                    return True
            return False

    def __eq__(self, other):
        """
        Takes a BST object as an argument.  Return True if self and other have equal root Nodes
        :param other: bst
        :return:
        """
        if not self.root and not other.root:
            return True
        if self.root and other.root:
            return self.root == other.root
        return False

    def sort(self):
        """
        Return a list of the data inselfin sorted orde
        :return:
        """
        if self.root:
            return self.root.sort([])
        else:
            return []

    @classmethod
    def from_file(cls, filename, type=None):
        """
        This classmethod takes a filename and a type (e.g. int, str, float, etc.) with a default value of None.
        Make a tree, open the file, add the value on each line to the tree, casting it first to the type
        argument if it is not None.  Return the tree
        :param filename:
        :param type:
        :return:
        """
        _cls = cls()
        f = open(filename)
        for line in f:
            if type:
                tree = type(line.strip(""))
                _cls + tree
            else:
                _cls + line.strip()
        f.close()
        return _cls


def selection_sort(lis):
    for i in range(len(lis) - 1):
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[i]:
                swap = lis[i]
                lis[i] = lis[j]
                lis[j] = swap
