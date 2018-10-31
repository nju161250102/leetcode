# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def fun(node):
            l = 0
            r = 0
            if node.left is not None:
                l = fun(node.left)
            if node.right is not None:
                r = fun(node.right)
            return max(l, r)+1
        
        if root is None:
            return 0
        
        return fun(root)
