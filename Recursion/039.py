def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res

def dfs(self, nums, target, index, path, res):
    if target == 0:
        res.append(path)
        return 
    for i in xrange(index, len(nums)):
        if nums[i]>target:
            break  # 避免进入递归
        self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
