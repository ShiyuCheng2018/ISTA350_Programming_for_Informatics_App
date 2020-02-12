'''
Author: Shiyu Cheng (23329948)
ISTA 350 Hw2
date: 02/12/2020
SL: Jacob Heller
In this homework, you will implement parse trees in two different ways: as a linked data
structure and as nested dictionaries. We will use the hot bills context again, but these
 classes can be adapted to store any sequences with only minor modifications. We will shortly
  explore in class why parse trees are so excellent for problems like this. They have a huge
   advantage over hw1's lists. What do you think it is?
'''


import numpy as np, re
from typing import List
import pandas as pd


class Node:
    def __init__(self, datum=None):
        '''
        This magic method takes an item to be stored in the Node instance that defaults to None.
        Initialize an instance variable called datum to the argument. Initialize an instance
        variable called children to the empty list.
        :param datum: string
        '''
        self.datum = datum
        self.children = []

    def get_child(self, datum=None):
        '''
        This instance method takes a key (search target) that defaults to None. If there is a child
         that contains the key, return it; otherwise return None.
        :param datum: string
        :return: node
        '''
        for child in self.children:
            if child.datum == datum:
                return child
        return None

    def __eq__(self, other):
        '''
        comparision
        :param other:
        :return:
        '''
        """
        The data comparison happens in get_child. This is strictly a helper method.
        """
        if len(self.children) != len(other.children):
            return False
        if not self.children:
            return True
        equal = True

        for child in self.children:
            other_child = other.get_child(child.datum)
            if not other_child:
                return False
            equal = equal and child == other_child
        return equal


class WatchListLinked:
    def __init__(self, filename=""):
        '''
        This magic method takes a filename that defaults to the empty string. Initialize an instance
         variable called root to a node that has 5 children. The datum in the node should be the None
          object (let your default arg do the work, don't pass it in). The data in the 5 children
          are the 5 denomination strings (i.e. '5', '10', etc.), respectively. The children have no
           children of their own. If a filename was passed in, each line of the file will represent
            a bill that we want to add to our watch list tree and will be in the format
             '<serial_number> <denomination>\n'. Look at one of the bill files in a text editor to
             see specific examples. Insert each of the bills into the watch list. Finally, an
             instance variable called validator holds a compiled regular expression that will be
             used to check for valid serial numbers (use the same regex as you did in hw1).
        :param datum: String
        '''
        self.root = Node()
        self.root.children = [Node('5'), Node('10'), Node('20'), Node('50'), Node('100')]
        self.validator = re.compile(r"^[A-M][A-L](?![0]{8})[0-9]{8}(?![O])[A-Y]$")
        # read files
        if filename:
            content = open(filename).readlines()
            for line in content:
                m_list = line.strip().split(" ")
                self.insert(m_list[0], m_list[1])

    def insert(self, serial_number, denomination):
        '''
        This instance method takes a string representing a serial number and a string representing
         a denomination. Insert the bill into the watch list. We will do this one in class, but it
          will not be posted. If you miss that class and you can't figure it out yourself, you will
           need to get it from another student.
        :param serial_number: string
        :param denomination: string
        :return: none
        '''
        current = self.root.get_child(denomination)
        for each in serial_number:
            next_node = current.get_child(each)
            if not next_node:
                next_node = Node(each)
                current.children.append(next_node)
            current = next_node
        if not current.get_child():
            current.children.append(Node())

    def search(self, serial_number, denomination):
        '''
        This instance method takes a string representing a serial number and a string representing a
         denomination. It returns True if the serial number is in the watch list, False otherwise.
         You should be able to implement this as a slight modification to insert.
        :param serial_number: string
        :param denomination: string
        :return:boolean
        '''

        current = self.root.get_child(denomination)
        for each in serial_number:
            next_node = current.get_child(each)
            if not next_node:
                return False
            current = next_node
        if not current.get_child():
            return False
        return True


class WatchListDict:
    def __init__(self, filename=""):
        '''
        This magic method takes a filename that defaults to the empty string. Initialize an instance
         variable called root to a dictionary that maps each of the 5 denomination strings
         (i.e. '5', '10', etc.) to an empty dictionary. If a filename was passed in, each line of
         the file will represent a bill that we want to add to our watch list dictionary and will be
          in the format '<serial_number> <denomination>\n'. Look at one of the bill files in a text
           editor to see specific examples. Insert each of the bills into the watch list. Finally,
           an instance variable called validator holds a compiled regular expression that will be
           used to check for valid serial numbers (use the same regex as you did in hw1).
        :param filename:string
        '''
        self.root = {'5':{}, '10':{}, '20':{}, '50':{}, '100':{}}
        self.validator = re.compile(r"^[A-M][A-L](?![0]{8})[0-9]{8}(?![O])[A-Y]$")
        # read files
        if filename:
            content = open(filename).readlines()
            for line in content:
                m_list = line.strip().split(" ")
                self.insert(m_list[0], m_list[1])

    def insert(self, serial_number, denomination):
        '''
        This instance method takes a string representing a serial number and a string representing
        a denomination. Insert the bill into the watch list. We will do this one in class, but it
         will not be posted. If you miss that class and you can't figure it out yourself, you will
          need to get it from another student.
        :param serial_number: string
        :param denomination: string
        :return: none
        '''
        current = self.root[denomination]

        for each in serial_number:
            if each not in current:
                current[each] = {}
            current = current[each]
        if None not in current:
            current[None] = None

    def search(self, serial_number, denomination):
        '''
        This instance method takes a string representing a serial number and a string representing
        a denomination. It returns True if the serial number is in the watch list, False otherwise.
         You should be able to implement this as a slight modification to insert.
        :param serial_number:string
        :param denomination:string
        :return:boolean
        '''
        current = self.root[denomination]
        for each in serial_number:
            if each not in current:
                return False
            current = current[each]
        if None in current:
            return True


def check_bills(watchlist, filename):
    '''
    This function takes a watch list instance of either class and a filename. The file contains a
    list of bills in the format '<serial_number> <denomination>\n' that we wish to check against our
     watch list. The method returns a list of bills in the format '<serial_number> <denomination>'.
      Go through the file line-by-line. If a bill is on the watch list, append it to the list of bad
       bills that you are building. It is also a bad bill if it has an invalid serial number. Return
        the list of bad bills. Why did we make this a function instead of instance methods in the
         classes?
    :param watchlist:string
    :param filename:string
    :return:list
    '''
    bad_bills = []
    content = open(filename).readlines()

    for line in content:
        bill = line.strip().split(" ")[0]
        denomination = line.strip().split(" ")[1]
        if not watchlist.validator.match(bill):
            bad_bills.append(line.strip())
        else:
            search = watchlist.search(bill, denomination)
            if search:
                bad_bills.append(line.strip())
    return bad_bills


def main():
    pass


if __name__ == '__main__':
    main()

