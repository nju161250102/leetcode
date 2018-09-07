class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num > 0:
                d[num] = True
        i = 1
        while True:
            if not d.has_key(i):
                return i
            i += 1