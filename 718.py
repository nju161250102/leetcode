class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        result = 0
        dp = []
        for i in range(n):
            dp.append([0] * n)
            
        for i in range(n):
            if A[i] == B[0]:
                dp[i][0] = 1
        
        for i in range(n):
            if A[0] == B[i]:
                dp[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result, dp[i][j])
        return result
