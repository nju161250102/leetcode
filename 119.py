class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def fun(m, n):
            if n == 0:
                return 1
            r = 1
            for i in range(m+1, n+1):
                r *= i
            for i in range(1, n-m+1):
                r /= i
            return r
        
        return [fun(i, rowIndex) for i in range(rowIndex+1)]