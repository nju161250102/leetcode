# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0].val <= right[0].val:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result += left
        if right:
            result += right
        return result
    
    def merge_sort(self, L):
        if len(L) <= 1:
            return L
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        # conquer sub-problem recursively
        return self.merge(left, right)
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head
        array = []
        while p is not None:
            array.append(p)
            p = p.next
        array = self.merge_sort(array)
        for i in range(len(array) - 1):
            array[i].next = array[i+1]
        array[len(array) - 1].next = None
        return array[0]
