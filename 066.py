class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += d
            d = 0
            if digits[i] > 9:
                d = 1
                digits[i] = 0
        if d == 1:
            digits.insert(0, d)
        return digits
