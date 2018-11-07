# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = _sum
        self.result = []
        self.array = []
        
        def fun(node):
            self.array.append(node.val)
            if node.left is None and node.right is None:
                if sum(self.array) == self.sum:
                    a = self.array[:]
                    self.result.append(a)
            if node.left is not None:
                fun(node.left)
            if node.right is not None:
                fun(node.right)
            del(self.array[-1])
        
        if root is None:
            return []
        fun(root)
        return self.result