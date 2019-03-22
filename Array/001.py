def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    s = {}
    for i in range(len(nums)):
        if s.has_key(nums[i]):
            # 不能重复取同一个元素
            if s[nums[i]] != i:
                return [i, s[nums[i]]]
        else:
            # 记录对应位置
            s[target - nums[i]] = i
