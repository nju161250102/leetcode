class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        c = 1
        while n > 1:
            d = b+c
            a = b
            b = c
            c = d
            n -= 1
        return c
