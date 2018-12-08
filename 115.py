class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = []
        for i in xrange(n+1):
            dp.append([0] * (m+1))
        for i in xrange(m):
            if s[i] == t[0]:
                dp[0][i] = 1
        
        for i in xrange(n):
            for j in xrange(m):
                if s[j] == t[i]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[n][m]
        