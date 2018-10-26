class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        def fun(l, r):
            if l == r:
                return False
            elif l == r - 1:
                return nums[l] == target
            else:
                c = (l+r)/2
                if nums[c] < nums[r-1] < target:
                    return fun(l, c)
                elif nums[l-1] < nums[c] < target:
                    return fun(c, r)
                return fun(l, c) or fun(c, r)
            
        return fun(0, len(nums))
