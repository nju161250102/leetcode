# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return root
        array = [root]
        
        while len(array) != 0:
            new_array = []
            for i in range(len(array)):
                node = array[i]
                if i + 1< len(array):
                    node.next = array[i+1]
                if node.left is not None:
                    new_array.append(node.left)
                if node.right is not None:
                    new_array.append(node.right)
            array = new_array