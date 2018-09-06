class Solution(object):
    def get_max(self, height):
        max_h = height[0]
        re = [max_h]
        for i in range(1, len(height)):
            if height[i-1] > height[i]:
                if not max_h or max_h < height[i-1]:
                    max_h = height[i-1]
            re.append(max_h)
        return re
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        if len(height) < 3:
            return 0
        
        left = self.get_max(height)
        right = list(reversed(self.get_max(list(reversed(height)))))
        for i in range(0, len(height)):
            if min(left[i], right[i]) > height[i]:
                result += (min(left[i], right[i]) - height[i])
        return result