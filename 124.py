# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.result = root.val
        def fun(node):
            leftMax = 0
            rightMax = 0
            if node.left is not None:
                leftMax = max(fun(node.left), 0)
            if node.right is not None:
                rightMax = max(fun(node.right), 0)
            if leftMax + rightMax + node.val > self.result:
                self.result = leftMax + rightMax + node.val
            sumMax = max(leftMax, rightMax)
            return max(leftMax, rightMax) + node.val
        fun(root)
        return self.result