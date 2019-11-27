#!/usr/bin/env python3

'''
leetCode
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
'''
class Solution(object):
    '''
    def __init__(self,name,score):
        self.str1 = str1
        self.str2 = str2
    '''
       
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        sameString = ''.join([a for a, b in list(zip(str1, str2)) if a == b])
        # print("The same part is ", sameString)
        for i in range(1, len(sameString)+1)[::-1]:
            #print("str1 is ", str1)
            #print("str2 is ", str2)
            #print("subString is ", sameString[:i])
            #print("split list1 is ",str1.split(sameString[:i]))
            #print("split list2 is ",str2.split(sameString[:i]))
            if not ''.join(str1.split(sameString[:i])) and not ''.join(str2.split(sameString[:i])):
                return sameString[:i]
        return ''
            



if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    s = Solution()
    print(" The result is ",s.gcdOfStrings(str1, str2))