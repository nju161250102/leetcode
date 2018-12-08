class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        k = 0
        while k <= r:
            if nums[k] == 0:
                nums[k], nums[l] = nums[l], nums[k]
                l += 1
                k += 1
            elif nums[k] == 2:
                nums[k], nums[r] = nums[r], nums[k]
                r -= 1
            else:
                k += 1