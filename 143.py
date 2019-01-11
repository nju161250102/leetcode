# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        array = []
        p = head
        while p is not None:
            array.append(p)
            # array[-1] = p
            p = p.next
        
        i = 0
        j = len(array) - 1
        while i < j:
            array[i].next = array[j]
            i += 1
            array[j].next = array[i]
            j -= 1
        array[i].next = None
