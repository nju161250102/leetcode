# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = True
        def fun(node):
            left = 0
            right = 0
            if node.left is None and node.right is None:
                return 1
            if node.left is not None:
                left = fun(node.left)
            if node.right is not None:
                right = fun(node.right)
            if abs(left-right) > 1:
                self.result = False
            return max(left, right)+1
        
        if root is None:
            return True
        fun(root)
        return self.result