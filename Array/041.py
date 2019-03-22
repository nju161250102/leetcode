def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    n = 0
    for k in nums:
        if k > 0:
            if k-n == 1:
                n = k
            elif k-n > 1:  # 提前结束遍历
                return n+1
    return n+1
