# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def fun(pl, pr, il, ir):
            if pl >= pr:
                return None
            root_node = TreeNode(preorder[pl])
            index = inorder.index(preorder[pl])
            root_node.left = fun(pl+1, pl+index+1-il, il, index)
            root_node.right = fun(pl+index+1-il, pr, index+1, ir)
            return root_node
        return fun(0, len(preorder), 0, len(inorder))
