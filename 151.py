class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        
        a = s.split(" ")
        a = [x for x in a if x != ""]
        a.reverse()
        return " ".join(a)
