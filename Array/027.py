def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    将需要删除的元素通过交换位置全部移至数组末尾
    """
    i = 0
    end = len(nums) - 1
    # 末尾向前跳过需要删除的元素，注意不能越界
    while end >= 0 and nums[end] == val:
        end -= 1
    # 向末尾遍历
    while i < end:
        if nums[i] == val:
            nums[i], nums[end] = nums[end], nums[i]  # 交换元素
            # 交换后向前跳过需要删除的元素
            while nums[end] == val:
                end -= 1
        i += 1
    return end + 1
