class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s) + 1):
            flag = False
            for j in range(i):
                flag = flag or (ok[j] == True and s[j:i] in wordDict)
            ok.append(flag)
        return ok[-1]
		
"""
The simple version:

def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]

Tips:
	The any() method returns True if any element of an iterable is True. If not, any() returns False
"""