class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def fun(re, left):
            for num in left:
                new_re = re + [num]
                new_left = left[:]
                new_left.remove(num)
                if len(new_left) == 0:
                    result.append(new_re)
                else:
                    fun(new_re, new_left)
        
        fun([], nums)
        return result