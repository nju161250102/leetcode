class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*sum(set(nums)) - sum(nums)) / 2
"""
The best answer is:
def singleNumber(self, nums):
    ones = 0
    twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

Explanation please see in discuss
"""
        