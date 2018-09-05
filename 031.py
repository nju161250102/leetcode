class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        next_nums = []
        p = len(nums) - 1
        while True:
            flag = False
            if len(next_nums) == 0:
                next_nums.append(nums[p])
            else:
                if nums[p] >= next_nums[-1]:
                    next_nums.append(nums[p])
                else:
                    n = nums[p]
                    for i in range(0, len(next_nums)):
                        if next_nums[i] > n:
                            nums[p] = next_nums[i]
                            next_nums[i] = n
                            break
                    p += 1
                    flag = True
            p -= 1
            if flag or p < 0:
                for i in range(p+1, len(nums)):
                    nums[i] = next_nums[i-p-1]
                break