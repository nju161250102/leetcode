class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        result = []
        k_max = (min(m, n) + 1) / 2
        i = -1
        j = -1
        for k in range(k_max):
            try:
                for i in range(k, n-k):
                    result.append(matrix[k][i])
                    if len(result) == m*n:
                        return result
                for i in range(k+1, m-k-1):
                    result.append(matrix[i][n-k-1])
                    if len(result) == m*n:
                        return result
                for i in range(n-k-1, k, -1):
                    result.append(matrix[m-k-1][i])
                    if len(result) == m*n:
                        return result
                for i in range(m-k-1, k, -1):
                    result.append(matrix[i][k])
                    if len(result) == m*n:
                        return result
            except:
                break
        return result
        