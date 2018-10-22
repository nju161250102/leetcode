# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBST(root, None, None)
        
    def isBST(self, root, low, high):
        if root is None:
            return True
        left = True
        right = True
        if low is not None:
            left = low < root.val
        if high is not None: 
            right = root.val < high
        if not (left and right):
            return False
        return self.isBST(root.left, low, root.val) and self.isBST(root.right, root.val, high)
 