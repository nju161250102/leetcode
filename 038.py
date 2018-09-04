class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for i in range(0, n-1):
            character = result[0]
            num = 0
            next_str = ""
            for c in result:
                if c == character:
                    num += 1
                else:
                    next_str += (str(num) + character)
                    character = c
                    num = 1
            if num != 0:
                next_str += (str(num) + character)
            result = next_str
        return result