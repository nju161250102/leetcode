class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)  == 1:
            return nums[0]
        
        if 0 in nums:
            index = nums.index(0)
            if index == 0:
                maxP = self.maxProduct(nums[1:])
            elif index == len(nums) - 1:
                maxP = self.maxProduct(nums[:-1])
            else:
                maxP = max(self.maxProduct(nums[:index]), self.maxProduct(nums[index+1:]))
            return max(0, maxP)
        
        first = None
        last = None
        n = 0
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            if nums[i] < 0:
                n += 1
                if first is None:
                    first = i
                last = i
        
        if n%2 == 0:
            return p
        else:
            left = 1
            right = 1
            for num in nums[:first+1]:
                left *= num
            for num in nums[last:]:
                right *= num
            return p / max(left, right)
