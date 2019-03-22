def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return len(nums)
    p = 0
    begin = 0  # 使用begin记录当前重复元素开始处
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            if i - begin > 1:
                # 重复了两次及以上
                nums[p] = nums[p+1] = nums[i-1]
                p += 2
            else:
                nums[p] = nums[i-1]
                p += 1
            begin = i
    # 最后再判断一次
    if len(nums) - begin > 1:
        nums[p] = nums[p+1] = nums[-1]
        p += 2
    else:
        nums[p] = nums[-1]
        p += 1
    return p
