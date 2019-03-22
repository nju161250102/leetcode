def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return 
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
