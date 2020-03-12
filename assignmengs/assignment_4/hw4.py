'''
Author: Shiyu Cheng (23329948)
ISTA 350 Hw4
date: 03/06/2020
SL: Jacob Heller
This homework is intended to acquaint you with Python’s operator overloading
functionality (magic methods) and the basics of binary integer arithmetic as it is
done inside in computers.
'''

class Binary:
    """
    If you use any method you have defined in another method definition, use the overloaded
     operator, if there is one. For instance, you will lose points if we see anything
     like bin1.__add__(bin2). This should be bin1 + bin2. Decorate your class with the
      functools.total_ordering decorator.
    """
    def __init__(self, my_str="0"):
        if my_str == "":
            self.my_str = "0"
        else:
            self.my_str = my_str
        self.bit_array = []

        if len(my_str) <= 16:
            for i in range(16 - len(self.my_str)):
                if self.my_str[0] == "1":
                    self.bit_array.append(1)
                else:
                    self.bit_array.append(0)
            for cha in self.my_str:
                if cha in ["0", "1"]:
                    self.bit_array.append(int(cha))
                else:
                    raise RuntimeError
        else:
            raise RuntimeError

    def __eq__(self, other):
        '''
        Takes a Binary object as an argument. Return True if self == the argument,
         False otherwise. You may not use int in this method. Do this one after init
          – many of the tests won't work until this one passes.
        :param other:
        :return:
        '''
        return self.bit_array == other.bit_array

    def __repr__(self):
        '''
        Return a 16-character string representing the fixed-width binary number,
        such as: '00000000000000000'.
        :return:
        '''
        concat = ""
        for cha in self.bit_array:
            concat += str(cha)
        return concat

    def __add__(self, other):
        '''
        Takes a Binary object as an argument. Return a new Binary instance that
         represents the sum of self and the argument. If the sum requires more than
          16 digits, raise a RuntimeError. You may not use int in this method.
        :param other:
        :return:
        '''
        maxlen = max(len(self.my_str), len(other.my_str))

        # Normalize lengths
        x = self.my_str.zfill(maxlen)
        y = other.my_str.zfill(maxlen)

        self.sum = ''
        carry = 0

        for i in range(maxlen - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            self.sum = ('1' if r % 2 == 1 else '0') + self.sum
            carry = 0 if r < 2 else 1

        if carry != 0:
            self.sum = '1' + self.sum

        return Binary(self.sum.zfill(maxlen))

    def __neg__(self):
        print("my_str: ",self.my_str)

        if self.my_str == "0":
            self.neg = self.my_str
            return Binary(self.neg)

        if len(self.my_str) > 1:
            if self.my_str[0] == "0":
                self.neg = "1" + str(self.my_str[1:])
            else:
                self.neg = "0" + str(self.my_str[1:])
        else:
            if self.my_str[0] == "0":
                self.neg = "1" + self.my_str
            else:
                self.neg = "0" + self.my_str

        print("neg: ",self.neg)
        return Binary(self.neg)

    def __sub__(self, other):
        pass
    def __int__(self):
        pass
    def it(self, binary):
        pass
    def __abs__(self):
        pass




def main():
    pass


if __name__ == '__main__':
    main()