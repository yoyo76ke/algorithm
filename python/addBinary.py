#!/usr/bin/env python3
from itertools import zip_longest
class Solution(object):
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        c = 0
        for (f, s) in zip_longest(a[::-1], b[::-1], fillvalue='0'):
            a = int(f)+int(s)+c
            d = a%2
            c = a//2
            res = str(d) + res
        if c > 0 :
            res = str(c) + res
        return res               


if __name__ == "__main__":
   
    a = "11"
    b = "1"
    s = Solution()
    print(" a is ", a)
    print(" b is ", b)
    print(" The result a+b is ", s.addBinary(a,b))

    