# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        layer = [root]
        while len(layer) > 0:
            for i in range(len(layer) / 2):
                if layer[i] is None and layer[len(layer) - i - 1] is None:
                    pass
                elif layer[i] is not None and layer[len(layer) - i - 1] is not None:
                    if layer[i].val != layer[len(layer) - i - 1].val:
                        return False
                else:
                    return False
            next_layer = []
            for node in layer:
                if node is not None:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            layer = next_layer
        return True
