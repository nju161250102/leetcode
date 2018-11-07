# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def fun(node):
            if node.left is not None and node.right is not None:
                lh, lt = fun(node.left)
                rh, rt = fun(node.right)
                node.right = lh
                lt.right = rh
                node.left = None
                return node, rt
            elif node.left is not None:
                lh, lt = fun(node.left)
                node.right = lh
                node.left = None
                return node, lt
            elif node.right is not None:
                rh, rt = fun(node.right)
                return node, rt
            else:
                return node, node
            
        if root is not None:    
            fun(root)  
