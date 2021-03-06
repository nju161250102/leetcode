class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle) - 1):
            triangle[i+1][0] += triangle[i][0]
            triangle[i+1][-1] += triangle[i][-1]
            for j in range(len(triangle[i]) - 1):
                triangle[i+1][j+1] += min(triangle[i][j], triangle[i][j+1])
            
        return min(triangle[-1])