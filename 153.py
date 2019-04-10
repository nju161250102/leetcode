def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = 0
    h = len(nums)-1
    while h>l:
        mid = (l+h) // 2
        if nums[mid] < nums[l]:
            h = mid
        elif nums[mid] > nums[h]:
            l = mid+1
        else:
            return nums[l]
    return nums[h]
