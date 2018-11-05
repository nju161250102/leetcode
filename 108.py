# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def fun(l, r):
            if l >= r:
                return None
            m = (l + r) / 2 
            node = TreeNode(nums[m])
            node.left = fun(l, m)
            node.right = fun(m+1, r)
            return node
        
        return fun(0, len(nums))