# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [root]
        result = []
        z_flag = False
        while len(l) > 0:
            next_l = []
            vals = []
            for node in l:
                if node is not None:
                    vals.append(node.val)
                    next_l.append(node.left)
                    next_l.append(node.right)
            l = next_l
            if z_flag:
                vals.reverse()
            z_flag = not z_flag
            if len(l) > 0:
                result.append(vals)
        return result
