'''
Author: Shiyu Cheng (23329948)
ISTA 350 Hw1
SL: Jacob Heller
This homework will introduce you to regular expressions and two types of search: linear
and binary. Later we will examine the advantages of each. For now, know that linear
search always works, but binary search requires a sorted sequence.
'''


import numpy as np, re
from typing import List
import pandas as pd


class WatchList:
    def __init__(self, filename="", ):
        '''
        class init
        :param filename:
        '''
        self.bills = {"5": [], "10": [], "20": [], "50": [], "100": []}
        self.is_sorted = True
        self.validator = re.compile(r"^[A-M][A-L](?![0]{8})[0-9]{8}(?![O])[A-Y]$")
        # make denomination dictionary
        if filename:
            content = open(filename).readlines()
            self.is_sorted = False
            for line in content:
                m_list = line.split(" ")
                self.bills[m_list[1].strip()].append(m_list[0])


    def insert(self, string):
        '''
        This instance method takes a string representing a bill in the format
         '<serial_number> <denomination>'. If the bills dictionary is sorted and the
          bill is not already in the dictionary, insert the new serial number into the
           appropriate list maintaining that list in sorted order. If the lists in the
            dictionary are not sorted and the bill is a new serial number, append it to
             the appropriate list.
        :param string: string
        :return:
        '''
        m_list = string.split(" ")
        key = m_list[1]
        value = m_list[0]

        if not self.is_sorted:
            self.bills[key].append(value)
        else:
            if self.bills[key] == [] or self.bills[key][-1] < value:
                self.bills[key].append(value)
            else:
                for each in self.bills[key]:
                    if value < each:
                        cur_index = self.bills[key].index(each)
                        list_1 = self.bills[key][0: cur_index]
                        list_1.append(value)
                        list_2 = self.bills[key][cur_index:]
                        self.bills[key] = list_1 + list_2
                        # denomination_array.insert(cur_index, value)
        print("deo: ", self.bills[key])

    def sort_bills(self):
        '''
        This instance method sorts the lists in the dictionary.
        :return:
        '''
        for key in self.bills.keys():
            self.bills[key] = sorted(self.bills[key])
        self.is_sorted = True


    def linear_search(self, string):
        '''
        This instance method takes a string representing a bill in the format
         '<serial_number> <denomination>'. Return True if it represents a bill in the
          dictionary, False otherwise.
        :param string: string
        :return: boolean
        '''
        m_list = string.split(" ")
        if m_list[0] in self.bills[m_list[1]]:
            return True
        return False

    def binary_search(self, string):
        '''
        This instance method takes a string representing a bill in the format '<serial_number>
        <denomination>'. Going through a sequence element-by-element searching for an item (the
        target of a search is called the key, in this case a serial number) is called linear or
         sequential search. If the sequence is sorted, there is a much faster technique called
          binary search. This method assumes that the lists in the dictionary are sorted. If the
           key is in the dictionary, return True, otherwise False. Here is some pseudocode for this method:
        :param string:
        :return: boolean
        '''
        denomination = string.split(" ")[1]
        goal = string.split(" ")[0]
        m_list = self.bills[denomination]
        # set low and high indices
        low = 0
        high = len(m_list) - 1

        while low <= high:
            mid = (low+high)//2
            if m_list[mid] == goal:
                return True
            elif m_list[mid] > goal:
                high = mid-1
            else:
                low = mid+1

        return False

    def check_bills(self, filename, boolean=False):
        '''
        This instance method takes a filename and a Boolean that defaults to False. The file
        contains a list of bills in the format '<serial_number> <denomination>\n' that we wish to
         check against our watch list. The method returns a list of bills in the format '<serial_number>
         <denomination>'. If the second argument is True, then you have to use binary search. Go through
          the file line-by-line. If a bill is on the watch list, append it to the list of bad bills that
           you are building. It is also a bad bill if it has an invalid serial number. Return the list of
           bad bills.
        :param filename: string
        :param boolean: boolean
        :return: list
        '''
        if boolean:
            self.sort_bills()
            self.is_sorted = boolean

        bad_bills = []
        content = open(filename).readlines()
        for line in content:
            bill = line.strip().split(" ")[0]
            if not self.validator.match(bill):
                bad_bills.append(line.strip())
            else:
                search = self.binary_search(line.strip()) if self.is_sorted else self.linear_search(line.strip())
                if search:
                    bad_bills.append(line.strip())
        return bad_bills


def main():
    pass


if __name__ == '__main__':
    main()
