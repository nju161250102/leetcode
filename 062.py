class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n]*m
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                result = 0
                if i == 0:
                    result = dp[i][j-1]
                elif j == 0:
                    result = dp[i-1][j]
                else:
                    result += 0 if obstacleGrid[i][j-1] == 1 else dp[i][j-1]
                    result += 0 if obstacleGrid[i-1][j] == 1 else dp[i-1][j]
                dp[i][j] = result
        return dp[m-1][n-1]