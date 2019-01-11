# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = []
        result = []
        node = root
        visit = None
        
        while node is not None:
            stack.append(node)
            node = node.left
            
        while len(stack) != 0:
            node = stack.pop()
            if node.right is None or node.right == visit:
                result.append(node.val)
                visit = node
            else:
                stack.append(node)
                node = node.right
                while node is not None:
                    stack.append(node)
                    node = node.left
                    
        return result