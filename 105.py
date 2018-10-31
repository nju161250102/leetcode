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
        def fun(preorder, inorder):
            if len(preorder) == 0:
                return None
            root_node = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root_node.left = fun(preorder[1:index+1], inorder[:index])
            root_node.right = fun(preorder[index+1:], inorder[index+1:])
            return root_node
        return fun(preorder, inorder)
