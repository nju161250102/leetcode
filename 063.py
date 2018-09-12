class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        i = n
        while i < m+n-1:
            a *= i
            i += 1
        i = 1
        while i < m:
            b *= i
            i += 1
        return a/b
        