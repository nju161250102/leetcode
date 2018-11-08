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
        k = 2
        
        for node in array:
            if len(array) == k - 1:
                for i in range(k/2-1, k-1):
                    array[i].next = array[i+1] if i+1 < k-1 else None
                k *= 2
            if node.left is not None:
                array.append(node.left)
            if node.right is not None:
                array.append(node.right)
