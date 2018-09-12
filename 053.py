class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        maxhere = nums[0]
        for i in range(1, len(nums)):
            if maxhere <= 0:
                maxhere = nums[i]
            else:
                maxhere += nums[i]
            if maxhere > maxsum:
                maxsum = maxhere
        return maxsum;
