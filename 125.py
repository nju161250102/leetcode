class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isChar(c):
            return ('a' <= c <= 'z') or ('0' <= c <= '9')
        
        front = 0
        end = len(s)
        s = s.lower()
        
        while front < end:
            if not isChar(s[front]):
                front += 1
            elif not isChar(s[end-1]):
                end -= 1
            else:
                if s[front] != s[end-1]:
                    return False
                front += 1
                end -= 1
                
        return True
