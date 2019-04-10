def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if not nums:
        return [-1, -1]
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            L, R = mid, mid
            while L >= l and nums[L] == target:
                L -= 1
            while R <= r and nums[R] == target:
                R += 1
            return [L+1, R-1]
        if nums[l] <= target < nums[mid]:
            r = mid -1
        else:
            l = mid +1

    return [-1, -1]
