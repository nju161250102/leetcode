class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        a_max = n/2
        b_max = (n+1)/2
        for a in range(a_max):
            for b in range(b_max):
                num = matrix[n-1-b][a]
                matrix[n-1-b][a] = matrix[n-1-a][n-1-b]
                matrix[n-1-a][n-1-b] = matrix[b][n-1-a]
                matrix[b][n-1-a] = matrix[a][b]
                matrix[a][b] = num