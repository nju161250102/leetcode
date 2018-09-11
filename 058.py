class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = i
        while i >= 0:
            if s[i] == ' ':
                return length - i
            i -= 1
        return length+1
 