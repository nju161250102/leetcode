# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def fun(il, ir, pl, pr):
            if pl >= pr:
                return None
            root_node = TreeNode(postorder[pr-1])
            index = inorder.index(postorder[pr-1])
            root_node.left = fun(il, index, pl, pl+index-il)
            root_node.right = fun(index+1, ir, pl+index-il, pr-1)
            return root_node
        return fun(0, len(inorder), 0, len(postorder))