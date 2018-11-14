# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.sum = 0
        num = 0
        # stack = [root]
        # numStack = [0]
        # while len(stack) != 0:
        #     node = stack.pop()
        #     num = numStack.pop()
        #     num = num * 10 + node.val
        #     if node.left is None and node.right is None:
        #         print(num)
        #         result += num
        #     if node.left is not None:
        #         stack.append(node.left)
        #         numStack.append(num)
        #     if node.right is not None:
        #         stack.append(node.right)
        #         numStack.append(num)
        def fun(node, num):
            num = num * 10 + node.val
            if node.left is None and node.right is None:
                self.sum += num
            if node.left is not None:
                fun(node.left, num)
            if node.right is not None:
                fun(node.right, num)
        
        fun(root, 0)
        return self.sum