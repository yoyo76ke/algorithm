#!/usr/bin/env python3
class Solution(object):
    """
    leetCode 13. Roman to Integer
    https://leetcode.com/problems/roman-to-integer/
    
    """
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToIntMap = {'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
        sum = 0
        for i in range(len(s)):
            #print("i is ", i)
            #print("Map[i] is ", romanToIntMap[s[i]])
            if sum != 0 and romanToIntMap[s[i-1]] < romanToIntMap[s[i]]:
                sum +=  romanToIntMap[s[i]] - 2* romanToIntMap[s[i-1]]
            else:
                sum +=  romanToIntMap[s[i]]
        return sum


if __name__ == "__main__":
    str1 = "IV"
    s = Solution()
    print(" The result is ", s.romanToInt(str1))