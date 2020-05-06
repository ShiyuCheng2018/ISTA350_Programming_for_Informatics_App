"""
Author: Shiyu Cheng (23329948)
ISTA 350 Hw4
date: 03/06/2020
SL: Jacob Heller
Summary: This homework is intended to acquaint you with Python’s operator overloading functionality (magic methods) and
the basics of binary integer arithmetic as it is done inside in computers. You have already been using operator
overloading, possibly without knowing what it’s called. For example, the plus sign is commonly and in Python used
to add numbers. But it is also used for string concatenation. That is an example of operator overloading. Special
note: many of the test methods will not work until your eq method is correct.

"""
import functools
import numpy as np


@functools.total_ordering
class Binary:
    """
    init has one string parameter with a default argument of '0'. This string can be the empty string (treat the
    same as '0'). Otherwise, it should consist only of 0’s and 1’s and should be 16 or less characters long. If
    the argument does not meet these requirements, raise a RuntimeError. Each Binary object has one instance
    variable, an integer array of length 16 called bit_array. bit_array has integers 0 or 1 in the same order
     as the corresponding characters in the argument. If the string is less than 16 characters long, bit_array
     should be padded on the left with the leftmost digit in the string (intified, of course). You may not use
      lists in this method.
    :param string:
    """

    def __init__(self, string='0'):
        if len(string) > 16:
            raise RuntimeError
        self.bit_array = np.zeros(16, dtype=int) if (string == "" or string[0] == '0') else np.ones(16, dtype=int)
        if string != "":
            for num in range(len(self.bit_array) - 1, 0, -1):
                if string != "":
                    if (string[-1] == '1') or (string[-1] == '0'):
                        self.bit_array[num] = string[-1]
                        string = string[0:-1]
                    else:
                        raise RuntimeError

    """
    Takes a Binary object as an argument. Return True if self == the argument, False otherwise. You may not use int in this
     method. Do this one after init – many of the tests won't work until this one passes.
    """

    def __eq__(self, other):
        return all(self.bit_array) == all(other.bit_array)

    """
    Return a 16-character string representing the fixed-width binary number, such as: '00000000000000000'.
    """

    def __repr__(self):
        return np.array2string(a=self.bit_array, separator="")[1:-1]

    """
    Takes a Binary object as an argument. Return a new Binary instance that represents the sum of self and the argument.
     If the sum requires more than 16 digits, raise a RuntimeError. You may not use int in this method.
    """

    def __add__(self, other):
        result_num = np.empty(16, dtype=int)
        carry = 0
        for i in range(15, -1, -1):
            bit_sum = self.bit_array[i] + other.bit_array[i] + carry
            result_num[i] = bit_sum % 2
            carry = bit_sum > 1
        if self.bit_array[0] == other.bit_array[0] != result_num[0]:
            raise RuntimeError("Binary: overflow")
        return Binary(''.join([str(i) for i in result_num]))

    """
    Return a new Binary instance that equals -self. You may not use int in this method.
    """

    def __neg__(self):
        copy_array = self.bit_array.copy()
        for i in range(len(self.bit_array)):
            if self.bit_array[i] == 1:
                copy_array[i] = 0
            else:
                copy_array[i] = 1
        my_str = ""
        for item in copy_array:
            my_str += str(item)
        amount = Binary(my_str) + Binary(str("0000000000000001"))
        return amount

    """
    Takes a Binary object as an argument. Return a new Binary instance that represents self the argument. You may not use 
    int in this method.
    """

    def __sub__(self, other):
        return self + (-other)

    """Return the decimal value of the Binary object. This method should never raise a RuntimeError due to overflow. Do
     not use int on Binary objects in any other method. You may use it to convert strings to integers, but not on Binary 
     objects. You will probably need to use the item method on the integer that you calculate to extract the regular 
     Python int from the np.int32 instance that you have created.
    """

    def __int__(self):
        _list = [0] * 16
        start = 1
        for i in range(1, 17, 1):
            _list[-i] = start
            start *= 2
        result = 0
        for i in range(len(self.bit_array)):
            if self.bit_array[i] == 1:
                result += _list[i]
        if self.bit_array[0] == 1:
            result = -(65536 - result)
        return result

    """
    Takes a Binary object as an argument. Return True if self < the argument, False otherwise. This method should never
     raise a RuntimeError due to overflow. You may not use int in this method.
    """

    def __lt__(self, other):
        neg_other = False
        if other.bit_array[0] == 1:
            other = -other
            neg_other = True
        total_self, total_other = 0, 0
        index = -1
        for i in range(0, 15):
            amount_other = other.bit_array[index]*2**i
            amount_self = self.bit_array[index]*2**i
            total_other += amount_other
            total_self += amount_self
            index -= 1
        if neg_other:
            total_other = -total_other
        return total_self < total_other

    """
    Takes a Binary object as an argument. Return a new Binary instance that represents the sum of self and the argument.
     If the sum requires more than 16 digits, raise a RuntimeError. You may not use int in this method.
    """

    def __abs__(self):
        if self.bit_array[0] == 0:
            my_str = ""
            for each in self.bit_array:
                my_str += str(each)
            return Binary(my_str)
        else:
            return (-self) + (-self) + (-self)
