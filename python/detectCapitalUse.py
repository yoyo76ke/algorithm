#!/usr/bin/env python3

class Solution(object):
    """
    leetCode 520. Detect Capital
    https://leetcode.com/problems/detect-capital/
    """
    def detectCapitalUse(self, word):
        """
        :type word : str
        :rtype : bool
        """
        return word.islower() or word.isupper() or word.istitle()



if __name__ == "__main__":
    str1 = "Ggg"
    s = Solution()
    print(" The result is ", s.detectCapitalUse(str1))