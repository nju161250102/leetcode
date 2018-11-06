# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def fun(node):
            left = 100000
            right = 100000
            if node.left is None and node.right is None:
                return 1
            if node.left is not None:
                left = fun(node.left)
            if node.right is not None:
                right = fun(node.right)
            return min(left, right)+1
        
        if root is None:
            return 0
        
        return fun(root)