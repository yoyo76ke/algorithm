#!/usr/bin/env python3
import re
class Solution(object):
    """
    leetCode 345. Reverse Vowels of a String
    https://leetcode.com/problems/reverse-vowels-of-a-string/
    """
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pattern = r"(?i)[aoeiu]"
        vowelList = re.findall(pattern, s)
        return re.sub(pattern,lambda m:vowelList.pop(), s)



    def reverseVowelsOne(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsList = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
        i = 0
        j = len(s)-1
        s = list(s)

        while i < j :
           
            while i < j and  not s[i] in vowelsList:
                i = i+1
                
            while j > i and not s[j] in vowelsList:
                j = j-1
            
            if i < j :
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        res = ''.join(s)
        return res

            

                


if __name__ == "__main__":
   
    magazine = "hello"
    s = Solution()
    print(" The result is ", s.reverseVowels(magazine))

    