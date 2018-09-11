class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = 0
        p_max = 0
        while p <= p_max < len(nums):
            if p + nums[p] > p_max:
                p_max = p + nums[p]
            p += 1
        return p_max >= len(nums) - 1
