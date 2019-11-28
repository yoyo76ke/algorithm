#!/usr/bin/env python3

class Solution(object):
    """
    leetCode 20. Valid Parentheses
    https://leetcode.com/problems/valid-parentheses/
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right, stack= "({[", ")}]", []
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if not stack or left.find(stack.pop()) != right.find(item):
                    return False
        return not stack
            

                


if __name__ == "__main__":
   
  
    b = "()"
    s = Solution()
    print(" The result is ", s.isValid(b))

    