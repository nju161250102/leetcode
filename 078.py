class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        v = [False] * n
        result = []
        
        def fun(k):
            result.append([nums[x] for x in range(n) if v[x]])
            for i in range(k, n):
                v[i] = True
                fun(i+1)
                v[i] = False
                
        fun(0)
        return result
