class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
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
        
        result = []
        for i in range(numRows):
            rowNum = []
            for j in range(i+1):
                rowNum.append(fun(j, i))
            result.append(rowNum)
        return result
