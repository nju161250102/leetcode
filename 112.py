# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, k):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.result = False
        self.array = []
        
        def fun(node, s):
            self.array.append(node.val)
            if node.left is None and node.right is None:
                if sum(self.array) == s:
                    self.result = True
            if node.left is not None:
                fun(node.left, s)
            if node.right is not None:
                fun(node.right, s)
            del(self.array[-1])
        
        if root is None:
            return False
        fun(root, k)
        return self.result
