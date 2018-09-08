class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        max_pos = 0
        for i in range(1, len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_pos = i
            else:
                if i - max_pos + nums[i] <= max_num:
                    nums[i] = None
        queue = []
        steps = [None] * len(nums)
        steps[0] = 0
        queue.append(0)
        
        while len(queue) != 0:
            v = queue[0]
            queue = queue[1:]
            for i in range(v+1, min(v+nums[v]+1, len(nums))):
                if steps[i] is None:
                    steps[i] = steps[v] + 1
                    if nums[i] is not None:
                        queue.append(i)
        return steps[-1]