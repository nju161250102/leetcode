def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ans = sys.maxint
    for i in xrange(len(nums)-1):
        # 还是使用双指针
        l = i+1
        r = len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s-target) < abs(ans-target):
                # 更新最接近的值
                ans = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return target
    return ans
