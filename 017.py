class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]
        
        if len(digits) == 0:
            return []
        for n in range(len(digits)):
            temp = []
            for s in result:
                for c in m[int(digits[n])-1]:
                    temp.append(s+c)
            result = temp
                
        return result