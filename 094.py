# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def fun(root):
            if root is None:
                return
            fun(root.left)
            result.append(root.val)
            fun(root.right)
        
        fun(root)
        return result
   