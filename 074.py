class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        i = 0
        while i < len(matrix) - 1:
            if target >= matrix[i+1][0]:
                i += 1
            else:
                break
        return target in matrix[i]
