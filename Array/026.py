def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
       return len(nums)
    p = 0
    for i in range(1, len(nums)):
        # 元素变化时记录元素，通过p指示位置
        if nums[i] != nums[i-1]:
            p += 1
            nums[p] = nums[i]
    return p + 1
