# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def fun(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self.fun(node.left, result)
        self.fun(node.right, result)
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        self.fun(root, r)
        return r
